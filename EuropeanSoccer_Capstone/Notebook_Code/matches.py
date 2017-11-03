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


def get_player_ratings_by_type(match_df, player_type_input, players_skills, SKILL_COLUMNS,
    players_ratings_label, last_date, team):
  # Away Team First
  n = 0
  ratings_sum = 0
  if team == 'away':
    PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
  else:
    PLAYER_COLUMNS = HOME_PLAYER_COLUMNS
  for AWAY_PLAYER_COLUMN in PLAYER_COLUMNS:
    player_api_id = match_df[AWAY_PLAYER_COLUMN]
    if math.isnan(player_api_id):
      print "Found a nan"
      continue
    player_type = players.player_api_id_to_player_type(players_skills=players_skills,
                  COLUMNS_OF_INTEREST= SKILL_COLUMNS, player_api_id = player_api_id)
    #print player_type['player_type'].values[0]
    if player_type not in PLAYER_TYPES:
      print "Bad category! " + player_type
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
                      SKILL_COLUMNS, players_skills, player_type_input, team_type ):
  last_date=match_df['date'].split(' ')[0]
  if match_df['id'] % 100 == 0:
    print "Done with " + str(match_df['id']) + "samples"
  rating = (get_player_ratings_by_type(match_df = match_df , player_type_input=player_type_input,
                                               players_skills=players_skills,SKILL_COLUMNS=SKILL_COLUMNS,
                                               players_ratings_label=players_ratings_label, last_date=last_date,
                                               team=team_type))

  return rating