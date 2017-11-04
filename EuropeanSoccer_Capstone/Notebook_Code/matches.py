from Utils import *
import datetime
import numpy as np
import players as players
import math

def result(match_df):
  if match_df['home_team_goal'] > match_df['away_team_goal']:
    return 'HOME_WIN'
  elif match_df['home_team_goal'] == match_df['away_team_goal']:
    return 'DRAW'
  else:
    return 'AWAY_WIN'


def get_player_ratings_by_type(match_df, player_type_input, player_to_player_type_dict,
    players_ratings_label, last_date, team):
  # Away Team First
  n = 0
  ratings_sum = 0
  if team == 'away':
    PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
  else:
    PLAYER_COLUMNS = HOME_PLAYER_COLUMNS
  for PLAYER in PLAYER_COLUMNS:
    player_api_id = match_df[PLAYER]
    # TODO: Get from dict
    player_type = player_to_player_type_dict[str(int(player_api_id))]
    if player_type not in PLAYER_TYPES:
      print "Unknown player type " + player_type
      raise Exception
    if player_type == player_type_input:
      n =n + 1
      rating_df = players.player_rating(player_api_id = player_api_id,
                                        last_date=last_date,
                                        players_ratings_label=players_ratings_label)
      ratings_sum = ratings_sum + rating_df['overall_rating'].values[0]

  if (n == 0):
    return 0
  else:
    type_rating = ratings_sum/n
    return type_rating


def single_match_rating(match_df, players_ratings_label,
          player_to_player_type_dict, player_type_input, team_type ):
  last_date=match_df['date'].split(' ')[0]
  if match_df[0] % 1000 == 0:
    print "Done with " + str(match_df['id']) + "samples"
  rating = (get_player_ratings_by_type(match_df = match_df , player_type_input=player_type_input,
                                              player_to_player_type_dict=player_to_player_type_dict,
                                               players_ratings_label=players_ratings_label, last_date=last_date,
                                               team=team_type))

  return rating