import numpy as np

'''
Function to fill nan for the teams' head to head home team win rate
'''

def fill_nan_head_2_head_home_team_win_rate(match_df, full_df):
  value = match_df['HEAD_2_HEAD_HOME_TEAM_WINS']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
      match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                     match_df['away_team_api_id'])]
    mean_home_win_rate = all_head_to_head_avg['HEAD_2_HEAD_HOME_TEAM_WINS'].mean(skipna=True)
    # If still Na, i.e. no history
    if np.isnan(mean_home_win_rate):
      mean_home_win_rate = 0.33
    return mean_home_win_rate


'''
Function to fill nan for the teams' head to head home team loss rate
'''

def fill_nan_head_2_head_home_team_loss_rate(match_df, full_df):
  value = match_df['HEAD_2_HEAD_HOME_TEAM_LOSS']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                               match_df['away_team_api_id'])]
    mean_home_loss_rate = all_head_to_head_avg['HEAD_2_HEAD_HOME_TEAM_LOSS'].mean(skipna=True)
    # If still Na, i.e. no history
    if np.isnan(mean_home_loss_rate):
      mean_home_loss_rate = 0.33
    return mean_home_loss_rate


'''
Function to fill nan for the teams' head to head draw rate
'''

def fill_nan_head_2_head_draw(match_df, full_df):
  value = match_df['HEAD_2_HEAD_DRAW']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                           match_df['away_team_api_id'])]
    mean_draw_rate = all_head_to_head_avg['HEAD_2_HEAD_DRAW'].mean(skipna=True)
    if np.isnan(mean_draw_rate):
      mean_draw_rate = 0.33
    return mean_draw_rate


'''
Function to fill nan for the home team's ALL TIME HOME RECORD
'''

def fill_nan_home_team_win_rate_all_time(match_df, full_df):
  value = match_df['HOME_WIN_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id'])]
    mean_home_win_rate = all_home_matches['HOME_WIN_RATE'].mean(skipna=True)
    return mean_home_win_rate

'''
Function to fill nan for the home team's ALL TIME HOME RECORD
'''

def fill_nan_away_team_win_rate_all_time(match_df, full_df):
  value = match_df['AWAY_WIN_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches = full_df[(full_df['away_team_api_id']==
                                    match_df['away_team_api_id'])]
    mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate


'''
Function to fill nan for the away team's away record THIS SEASON
'''

def fill_nan_away_team_win_rate_this_season(match_df, full_df):
  value = match_df['AWAY_WIN_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_this_season = full_df[(full_df['away_team_api_id']==
                                match_df['away_team_api_id']) &
                               (full_df['season']==
                                match_df['season'])]
    mean_away_win_rate = all_away_matches_this_season['AWAY_WIN_RATE_THIS_SEASON'].mean(skipna=True)
    if np.isnan(mean_away_win_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate


'''
Function to fill nan for the home team's home record THIS SEASON
'''

def fill_nan_home_team_win_rate_this_season(match_df, full_df):
  value = match_df['HOME_WIN_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches_this_season = full_df[(full_df['home_team_api_id']==
                                            match_df['home_team_api_id']) &
                                           (full_df['season']==
                                            match_df['season'])]
    mean_home_win_rate = all_home_matches_this_season['HOME_WIN_RATE_THIS_SEASON'].mean(skipna=True)
    return mean_home_win_rate

'''
Function to fill nan for the away team's ALL TIME AWAY RECORD at this ground
'''

def fill_nan_away_team_win_rate_all_time_at_this_ground(match_df, full_df):
  value = match_df['AWAY_WIN_RATE_AT_THIS_GROUND']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_at_this_ground = full_df[(full_df['away_team_api_id']==
                                    match_df['away_team_api_id']) &
                                   (full_df['home_team_api_id']==
                                    match_df['home_team_api_id'])]

    mean_away_win_rate = all_away_matches_at_this_ground['AWAY_WIN_RATE_AT_THIS_GROUND'].mean(skipna=True)
    if np.isnan(mean_away_win_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate

