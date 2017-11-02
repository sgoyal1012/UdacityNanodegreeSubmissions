from Utils import *
import datetime
import numpy as np


'''
Classify players into midfield, defense, attacking
'''
def player_to_player_type(players_skills, player_names_df, player_name,
    COLUMNS_OF_INTEREST):
  """
  Takes in as an input the relevant player skills and classifies into
  midfielder, attacker, defender or goalie; based on the most recent numbers
  from the database.
  """
  player_join_df = pd.merge(players_skills, player_names_df, on='player_api_id',
                            how='outer')
  my_player_df = (
    player_join_df[player_join_df['player_name'].str.contains(player_name)])
  most_recent_date = my_player_df['date'].max()
  latest_df = my_player_df[my_player_df['date'] == most_recent_date]
  latest_skills_df = latest_df[['finishing', 'sliding_tackle',
                                  'gk_reflexes', 'short_passing']]
  # TODO: Convert this to lambda function; see matches.result method
  latest_skills_df['player_type'] = latest_skills_df.idxmax(axis=1)
  latest_skills_df['player_name'] = player_name
  latest_skills_df['player_api_id'] = latest_df['player_api_id']
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'finishing', 'Attacker', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'short_passing', 'Midfielder', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'sliding_tackle', 'Defender', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'gk_reflexes', 'Goalkeeper', latest_skills_df['player_type'])

  return latest_skills_df[['player_name', 'player_type', 'player_api_id']]

def player_api_id_to_player_type(players_skills, COLUMNS_OF_INTEREST, player_api_id):
  """
  Takes in as an input the relevant player skills and classifies into
  midfielder, attacker, defender or goalie; based on the most recent numbers
  from the database.
  """
  my_player_df = players_skills[players_skills['player_api_id'] == player_api_id]
  most_recent_date = my_player_df['date'].max()
  latest_df = my_player_df[my_player_df['date'] == most_recent_date]
  latest_skills_df = latest_df[COLUMNS_OF_INTEREST]
  # TODO: Convert this to lambda function; see matches.result method
  latest_skills_df['player_type'] = latest_skills_df.idxmax(axis=1)
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'finishing', 'Attacker', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'short_passing', 'Midfielder', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'sliding_tackle', 'Defender', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'gk_reflexes', 'Goalkeeper', latest_skills_df['player_type'])

  return latest_skills_df[['player_type']]

def player_rating(player_api_id, last_date, players_ratings_label):
  """
  Gets the rating for a season for a player_api_id, based on the closest date
  :param player_api_id:
  :return:
  """
  all_player_ratings_df = players_ratings_label[
    players_ratings_label['player_api_id'] == player_api_id]
  pivot = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
  all_player_ratings_df.date = pd.to_datetime(all_player_ratings_df.date)
  min_date = (nearest(all_player_ratings_df.date, pd.to_datetime(last_date)))
  return all_player_ratings_df[all_player_ratings_df.date == min_date]

def nearest(items, pivot):
  value = min(items, key=lambda x: abs(pivot - x))
  return value

def average_team_rating(match_df):
  return None
