import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import py7zr
import tempfile
import os
import seaborn as sns
import plotly.figure_factory as ff
import preprocessor, helper

archive_path = 'athlete_events.7z'
csv_filename = 'athlete_events.csv'

with tempfile.TemporaryDirectory() as temp_dir:
    with py7zr.SevenZipFile(archive_path, mode='r') as archive:
        extracted_files = archive.extract(path=temp_dir)

    print("Extracted files:", os.listdir(temp_dir))

    csv_file_path = os.path.join(temp_dir, csv_filename)

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File not found: {csv_file_path}")
    
    athlete_df = pd.read_csv(csv_file_path)
    
#athlete_df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

data = preprocessor.preprocess(athlete_df, region_df)

st.sidebar.title('Olympic History Analysis')
st.sidebar.image('https://w7.pngwing.com/pngs/1020/402/png-transparent-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport-logo.png')
st.sidebar.image('https://i.pinimg.com/736x/18/1c/ea/181cea03aee058fafc493e616ca37451.jpg')

user_choice = st.sidebar.radio(
    'Select an option', ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

if user_choice == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, countries = helper.country_year_list(data)

    selected_year = st.sidebar.selectbox('Select a Year for analysis', years)
    selected_country = st.sidebar.selectbox('Select a Country for analysis', countries)

    medal_tally = helper.fetch_medal_tally(data, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Tally')

    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.title('Overall Medal Tally for '+selected_country)

    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.title('Medal Tally in '+ str(selected_year) +' Olympics')

    else:
        st.title(selected_country+' Performance in '+ str(selected_year) +' Olympics')

    st.table(medal_tally)

if user_choice == 'Overall Analysis':
    editions = data['Year'].unique().shape[0]-1
    cities = data['City'].unique().shape[0]
    sports = data['Sport'].unique().shape[0]
    events = data['Event'].unique().shape[0]
    athletes = data['Name'].unique().shape[0]
    nations = data['region'].unique().shape[0]

    st.title('Olympic Stats')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    nations_over_time = preprocessor.data_over_time(data,'region')
    fig = px.line(nations_over_time, x='Editions', y='No. of region')
    st.title('Participating Nations Over The Years')
    st.plotly_chart(fig)

    events_over_time = preprocessor.data_over_time(data, 'Event')
    fig = px.line(events_over_time, x='Editions', y='No. of Event')
    st.title('Number of Events Over The Years')
    st.plotly_chart(fig)

    athlete_over_time = preprocessor.data_over_time(data, 'Name')
    fig = px.line(athlete_over_time, x='Editions', y='No. of Name')
    st.title('Number of Athletes Participated Over The Years')
    st.plotly_chart(fig)

    st.title('No. of Event over time (Every Sport)')
    fig, ax = plt.subplots(figsize=(20, 20))
    x = data.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True, cmap='viridis')
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sport_list = data['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    success_athletes = preprocessor.most_successful(data, selected_sport)
    st.table(success_athletes)

if user_choice == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')
    country = data['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0, 'Overall')

    selected_country_value = st.sidebar.selectbox('Select a country', country)

    country_df = preprocessor.yearwise_medal_tally(data, selected_country_value)
    fig = px.line(country_df, x='Year', y='Total Medals')
    st.title(selected_country_value + ' Medal Tally Over The Years')
    st.plotly_chart(fig)

    st.title(selected_country_value + ' excels in the following sports')
    pivot = preprocessor.country_event_heatmap(data, selected_country_value)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pivot,annot=True)
    st.pyplot(fig)

    st.title('Top 15 athletes of '+ selected_country_value)
    top_15_df = helper.most_successful_countrywise(data, selected_country_value)
    st.table(top_15_df)

if user_choice == 'Athlete-wise Analysis':
    data_df = data.drop_duplicates(subset=['Name', 'region'])

    data_df.dropna(subset=['Age'], inplace=True)

    data_df['Age'] = data_df['Age'].astype('int')

    x1 = data_df['Age'].dropna()
    x2 = data_df[data_df['Gold'] == 1]['Age'].dropna()
    x3 = data_df[data_df['Bronze'] == 1]['Age'].dropna()
    x4 = data_df[data_df['Silver'] == 1]['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    list_val = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Equestrianism',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Modern Pentathlon', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens', 'Trampolining',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Lacrosse', 'Polo',
                     'Cricket', 'Ice Hockey', 'Racquets', 'Croquet', 'Figure Skating',
                     'Jeu De Paume', 'Roque', 'Motorboating', 'Basque Pelota',
                     'Alpinism', 'Aeronautics']

    for sport in famous_sports:
        temp_df = data_df[data_df['Sport'] == sport]
        ages = temp_df[temp_df['Gold'] == 1]['Age'].dropna().values

        if ages.size > 50:
            list_val.append(ages)
            name.append(sport)

    fig = ff.create_distplot(list_val, name, show_hist=False, show_rug=False)
    st.title('Distribution of Age w.r.t Sports (Gold Medalist)')
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

    sport_list = data_df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Sport-wise Athletes Height vs Weight Analysis')

    selected_sport = st.selectbox('Select a Sport', sport_list)

    temp_df = helper.weight_vs_height(data_df, selected_sport)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x='Weight', y='Height', hue='Gold', data=temp_df, style='Sex', s=75)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x='Weight', y='Height', hue='Silver', data=temp_df, style='Sex', s=75)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x='Weight', y='Height', hue='Bronze', data=temp_df, style='Sex', s=75)
    st.pyplot(fig)

    st.title('Men vs Women Participation over the Years')
    final = helper.men_vs_women(data_df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
