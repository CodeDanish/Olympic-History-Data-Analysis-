import matplotlib.pyplot as plt
import seaborn as sns


def medal_tally(data):
    medal_tally = data.drop_duplicates(
        subset=['Teams', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Bronze', 'Gold', 'Silver'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(
        by='Gold', ascending=False).reset_index()

    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally


def country_year_list(data):
    years = data['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    data.dropna(subset=['region'], inplace=True)
    countries = data['region'].unique().tolist()
    countries.sort()
    countries.insert(0, 'Overall')
    return years, countries


def fetch_medal_tally(data, year, country):
    flag = 0
    medal_df = data.drop_duplicates(
        subset=['Teams', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Bronze', 'Gold', 'Silver'])

    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df

    elif year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]

    elif year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == year]

    else:
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == year)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold',
                                                                                      ascending=False).reset_index()

    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x


def most_successful_countrywise(df, country):
    temp_df = df[df['No Medal'] != 1]

    temp_df = temp_df[temp_df['region'] == country]

    success_df = temp_df['Name'].value_counts().reset_index().head(15).merge(df, on='Name', how='left')[
        ['Name', 'count', 'Sport']]
    success_df.rename(columns={'count': 'No. of Medals'}, inplace=True)
    return success_df.drop_duplicates()


def weight_vs_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name','region'])

    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df


def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)
    final['Female'] = final['Female'].astype(int)

    return final
