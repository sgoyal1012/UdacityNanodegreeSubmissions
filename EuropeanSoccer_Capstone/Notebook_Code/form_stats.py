import pandas as pd
import numpy as np
from functools import partial

'''
Function to get the home record (win rate) for the home team prior to the date today
'''
def home_team_all_time_home_record(match_df, full_df):
  all_team_home_matches_before_today = full_df[(match_df['date'] >
          full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_home_matches_before_today == 0:
    return np.nan

  all_team_home_wins_before_today = full_df[(match_df['date'] >
           full_df['date']) & (full_df['home_team_api_id']==
      match_df['home_team_api_id']) & (full_df['result_label'] == "HOME_WIN")].shape[0]
  return np.true_divide(all_team_home_wins_before_today, all_team_home_matches_before_today)


'''
Function to get the home record (win rate) for the home team prior to this date today; FOR THIS SEASON
'''
def home_team_this_season_home_record(match_df, full_df):
  all_team_home_matches_this_season = full_df[(match_df['date'] >
                                               full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                              (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_home_matches_this_season == 0:
    return np.nan

  all_team_home_wins_this_season = full_df[(match_df['date'] >
                                            full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                           (full_df['result_label'] == "HOME_WIN") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_home_wins_this_season, all_team_home_matches_this_season)


'''
AWAY TEAM FUNCTIONS
'''
'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_record(match_df, full_df):
  all_team_away_matches_before_today = full_df[(match_df['date'] >
                                                full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today == 0:
    return np.nan

  all_team_away_wins_before_today = full_df[(match_df['date'] >
                                             full_df['date']) & (full_df['away_team_api_id']==
           match_df['away_team_api_id']) & (full_df['result_label'] == "AWAY_WIN")].shape[0]
  return np.true_divide(all_team_away_wins_before_today, all_team_away_matches_before_today)

'''
Function to get the away record (win rate) for the away team prior to this date today; FOR THIS SEASON
'''
def away_team_this_season_away_record(match_df, full_df):
  all_team_away_matches_this_season = full_df[(match_df['date'] >
      full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
                                 (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_away_matches_this_season == 0:
    return np.nan

  all_team_away_wins_this_season = full_df[(match_df['date'] >
             full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
      (full_df['result_label'] == "AWAY_WIN") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_away_wins_this_season, all_team_away_matches_this_season)

'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_record_at_this_ground(match_df, full_df):
  all_team_away_matches_before_today_at_this_ground = full_df[(match_df['date'] >
                    full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])
                    & (match_df['home_team_api_id'] == full_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today_at_this_ground == 0:
    return np.nan

  all_team_away_wins_before_today_at_this_ground = full_df[(match_df['date'] >
                               full_df['date']) & (full_df['away_team_api_id']== match_df['away_team_api_id']) &
                   (match_df['home_team_api_id'] == full_df['home_team_api_id']) & (full_df['result_label'] == "AWAY_WIN")].shape[0]
  return np.true_divide(all_team_away_wins_before_today_at_this_ground, all_team_away_matches_before_today_at_this_ground)


'''
FUNCTION TO GET HEAD TO HEAD in terms of (Home team win percentage, home team lose percentage, draws)
'''
def head_to_head(match_df, full_df, value):
  # Either team can be home or away
  this_fixture_all_count = full_df[(match_df['date'] > full_df['date']) &
   ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))].shape[0]
  this_fixture_all_home_team_wins = full_df[(match_df['date'] > full_df['date']) &
          ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'HOME_WIN')].shape[0]
  this_fixture_all_home_team_losses = full_df[(match_df['date'] > full_df['date']) &
                                            ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'AWAY_WIN')].shape[0]
  this_fixture_all_draws = full_df[(match_df['date'] > full_df['date']) &
                                            ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'DRAW')].shape[0]

  return_fixture_all_count = full_df[(match_df['date'] > full_df['date']) &
   ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))].shape[0]
  return_fixture_all_home_team_wins = full_df[(match_df['date'] > full_df['date']) &
       ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'AWAY_WIN')].shape[0]
  return_fixture_all_home_team_losses = full_df[(match_df['date'] > full_df['date']) &
                                              ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'HOME_WIN')].shape[0]
  return_fixture_all_draws = full_df[(match_df['date'] > full_df['date']) &
                                              ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'DRAW')].shape[0]

  total_home_wins = this_fixture_all_home_team_wins + return_fixture_all_home_team_wins
  total_home_losses = this_fixture_all_home_team_losses + return_fixture_all_home_team_losses
  total_draws = this_fixture_all_draws+ return_fixture_all_draws
  total_head_to_head = this_fixture_all_count + return_fixture_all_count
  # No history
  if total_head_to_head == 0:
    return np.nan
  if (total_home_wins + total_home_losses + total_draws != total_head_to_head):
    raise Exception

  home_win_ratio = np.true_divide(total_home_wins, total_head_to_head)
  home_loss_ratio = np.true_divide(total_home_losses, total_head_to_head)
  draw_ratio = np.true_divide(total_draws, total_head_to_head)
  if value == "Home Win":
    return home_win_ratio
  elif value == "Home Loss":
    return home_loss_ratio
  else:
    return draw_ratio

if __name__ == '__main__':
  all_features_df = pd.read_csv('Data_Structures/MATCH_FEATURES.csv')
  FORM_STATS_FEATURES = ['match_api_id', 'home_team_api_id', 'away_team_api_id',
                       'season', 'date', 'result_label']
  all_features_df['date'] = pd.to_datetime(all_features_df['date'])

  match_sample = all_features_df

  print "Getting head to head home win rate"
  get_head_to_head = partial(head_to_head, full_df=all_features_df, value = "Home Win")
  match_sample['HEAD_2_HEAD_HOME_TEAM_WINS'] = match_sample.apply(get_head_to_head, axis = 1)

  print "Getting head to head home loss rate"
  get_head_to_head = partial(head_to_head, full_df=all_features_df, value = "Home Loss")
  match_sample['HEAD_2_HEAD_HOME_TEAM_LOSS'] = match_sample.apply(get_head_to_head, axis = 1)

  print "Getting head to head draw rate"
  get_head_to_head = partial(head_to_head, full_df=all_features_df, value = "Draw")
  match_sample['HEAD_2_HEAD_DRAW'] = match_sample.apply(get_head_to_head, axis = 1)

  print "Getting home win rate all time"
  get_home_win_rate = partial(home_team_all_time_home_record, full_df=all_features_df)
  match_sample['HOME_WIN_RATE'] = match_sample.apply(get_home_win_rate, axis = 1)

  print "Getting home win rate this season"
  get_home_win_rate_this_season = partial(home_team_this_season_home_record, full_df=all_features_df)
  match_sample['HOME_WIN_RATE_THIS_SEASON'] = match_sample.apply(get_home_win_rate_this_season, axis = 1)

  print "Getting away win rate all time"
  get_away_win_rate = partial(away_team_all_time_away_record, full_df=all_features_df)
  match_sample['AWAY_WIN_RATE'] = match_sample.apply(get_away_win_rate, axis = 1)

  print "Getting away win rate this season"
  get_away_win_rate_this_season = partial(away_team_this_season_away_record, full_df=all_features_df)
  match_sample['AWAY_WIN_RATE_THIS_SEASON'] = match_sample.apply(get_away_win_rate_this_season, axis = 1)

  print "Getting away team's win rate AT THIS GROUND"
  get_away_win_rate_at_this_ground = partial(away_team_all_time_away_record_at_this_ground, full_df=all_features_df)
  match_sample['AWAY_WIN_RATE_AT_THIS_GROUND'] = match_sample.apply(get_away_win_rate_at_this_ground, axis = 1)


  match_sample.to_csv('Data_Structures/form_numbers.csv')