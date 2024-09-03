import numpy as np
import pandas as pd


def preprocess(athlete_df, region_df):
    athlete = athlete_df[athlete_df['Season'] == 'Summer']

    athlete = athlete.merge(region_df, on='NOC', how='left')

    athlete.drop_duplicates(inplace=True)

    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder(sparse_output=False)
    medal = ohe.fit_transform(athlete[['Medal']])
    medal = medal.astype(int)

    athlete = np.hstack((athlete[[
                             'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season',
                              'City', 'Sport', 'Event', 'region', 'notes']].values, medal))
    athlete = pd.DataFrame(athlete)

    athlete.rename(
        columns={0: 'ID', 1: 'Name', 2: 'Sex', 3: 'Age', 4: 'Height', 5: 'Weight', 6: 'Teams', 7: 'NOC', 8: 'Games',
                 9: 'Year', 10: 'Season', 11: 'City', 12: 'Sport', 13: 'Event', 14: 'region', 15: 'notes', 16: 'Bronze',
                 17: 'Gold', 18: 'Silver', 19: 'No Medal'}, inplace=True)

    athlete['Year'] = athlete['Year'].astype('str')

    return athlete


def data_over_time(data, col):
    data_by_year = data.drop_duplicates(['Year', col])[
        'Year'].value_counts().reset_index().sort_values(by='Year')

    data_by_year.rename(columns={'Year': 'Editions', 'count': 'No. of '+col },
                                         inplace=True)

    return data_by_year


def most_successful(df, sport):
    temp_df = df[df['No Medal'] != 1]

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    success_df = temp_df['Name'].value_counts().reset_index().head(15).merge(df, on='Name', how='left')[[
        'Name', 'count', 'Sport', 'region']]
    success_df.rename(columns={'count': 'No. of Medals'}, inplace=True)

    return success_df.drop_duplicates()


def yearwise_medal_tally(df, country):
    medal_winners = df[df['No Medal'] != 1]
    
    medal_winners.drop_duplicates(subset=['Year','NOC','Games','Year','City','Sport','Event','Bronze','Gold',
                                          'Silver'],inplace=True)

    new_medal_df = medal_winners[medal_winners['region'] == country]
    final_df = new_medal_df.groupby('Year')[['Bronze', 'Gold', 'Silver']].sum().reset_index()
    final_df['Total Medals'] = final_df['Bronze'] + final_df['Gold'] + final_df['Silver']
    new_final_df = final_df[['Year', 'Total Medals']]

    return new_final_df


def country_event_heatmap(df, country):
    medal_winners = df[df['No Medal'] != 1]

    medal_winners.drop_duplicates(subset=['Year', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Bronze', 'Gold',
                                          'Silver'], inplace=True)

    new_medal_df = medal_winners[medal_winners['region'] == country]
    final_df = new_medal_df.groupby(['region', 'Sport', 'Year'])[['Bronze', 'Gold', 'Silver']].sum().reset_index()
    final_df['Total Medals'] = final_df['Bronze'] + final_df['Gold'] + final_df['Silver']

    new_final_df = final_df[['region', 'Sport', 'Year', 'Total Medals']]

    pivot = new_final_df.pivot_table(index='Sport', values='Total Medals', columns='Year').fillna(0)
    return pivot



