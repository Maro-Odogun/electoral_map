import geopandas as gpd
import pandas as pd

### Presidential Election Data 
election_results_23 = pd.read_csv('data/Nigeria Map 2023.csv')
states = gpd.read_file('data/Nigeria State Boundaries.geojson')
states = states[['admin1Name', 'geometry']]

main_data_23 = states.merge(election_results_23, left_on='admin1Name', right_on='Region Name', how='inner').set_index('Region Name').drop('admin1Name', axis=1)
main_data_23['Year'] = 2023

election_results_19 = pd.read_csv('data/Election Map 2019.csv')
main_data_19 = states.merge(election_results_19, left_on='admin1Name', right_on='Region Name', how='inner').set_index('Region Name').drop('admin1Name', axis=1)
main_data_19['Year'] = 2019

election_results_15 = pd.read_csv('data/Nigeria Map 2015.csv')
main_data_15 = states.merge(election_results_15, left_on='admin1Name', right_on='Region Name', how='inner').set_index('Region Name').drop('admin1Name', axis=1)
main_data_15['Year'] = 2015

main_data = pd.concat([main_data_23, main_data_19, main_data_15])


### Senate and House of Reps Data
senate_house = pd.read_excel('data/Senate National Assembly.xlsx', sheet_name=[0,1])
senate_df = senate_house[0]
house_df = senate_house[1]


### Voter Participation Data
voter_reg = pd.read_csv('data/Nigeria Elections Voter Metrics.csv')
voter_reg_focus = voter_reg.loc[:, ['Year', '% registered voters who voted',
 '% eligible pop. who registered to vote', '% eligible pop. who voted']]


