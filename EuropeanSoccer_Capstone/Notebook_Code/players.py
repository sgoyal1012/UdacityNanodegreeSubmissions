from Utils import *
import datetime
'''
Classify players into midfield, defense, attacking
'''


def classify_players(player_df):
  return None


def players_to_player_type(players_skills, player_names_df, player_name):
  """
  Takes in as an input the relevant player skills and classifies into
  midfielder, attacker, defender or goalie; based on the most recent numbers
  from the database.
  """
  player_join_df = pd.merge(players_skills, player_names_df, on='player_api_id',
                            how='outer')
  COLUMNS_OF_INTEREST = ['player_name', 'finishing', 'sliding_tackle',
                         'gk_reflexes']
  my_player_df = (
    player_join_df[player_join_df['player_name'].str.contains(player_name)])
  most_recent_date = my_player_df['date'].max()
  return (my_player_df[my_player_df['date'] == most_recent_date])[
    COLUMNS_OF_INTEREST]


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
