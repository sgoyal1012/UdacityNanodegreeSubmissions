import pandas as pd

feature_1_df = pd.read_csv('match_features_so_far.csv')
feature_2_df = pd.read_csv('match_features_so_far_2.csv')


JOIN_COLUMNS = ['match_api_id', 'home_team_api_id', 'away_team_api_id',
                'season', 'date', 'result_label']

all_feature_df = pd.merge(feature_1_df, feature_2_df,  how='left',
                  left_on=JOIN_COLUMNS, right_on=JOIN_COLUMNS)

all_feature_df.to_csv('Data_Structures/MATCH_FEATURES.csv')