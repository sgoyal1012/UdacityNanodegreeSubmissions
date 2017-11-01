from Utils import *
import datetime
import numpy as np


def result(match_df):
  if match_df['home_team_goal'] > match_df['away_team_goal']:
    return 'HOME_WIN'
  elif match_df['home_team_goal'] == match_df['away_team_goal']:
    return 'DRAW'
  else:
    return 'AWAY_WIN'
