import zipfile
from Utils import *
import sqlite3
import pandas as pd


def uncompress_and_open_sqlite():
  zip = zipfile.ZipFile(INPUTFILE_DIR + INPUTZIPFILE)
  zip.extractall(path=INPUTFILE_DIR)
  conn = sqlite3.connect(INPUTFILE_DIR + DATABASENAME)
  return conn


def execute_query_print_results(conn, sql_query):
  cur = conn.cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()
  for row in rows:
    print row


def desc_table(table_df, table_name):
  print SEPARATOR
  print "For table " + table_name + " there are " + str(table_df.shape[0]) + \
        " entries with "+ str(table_df.shape[1]) + " features"
  print table_df.columns.tolist()
  print SEPARATOR


'''
Classify players into midfield, defense, attacking
'''
def classify_players(player_df):
  return None


def home_advantage(matches_df, conn):
    # TODO: Convert to DataFrama and Plot
   country_id_to_num_matches = matches_df.groupby(['country_id']).size().to_dict()
   countries_df = sql_to_dataframe(conn, select_all_query_table("Country"))
   for country_id in country_id_to_num_matches:
     print map_country_to_name(countries_df, country_id).to_string(), " :", str(country_id_to_num_matches[country_id])


def players_to_work_rate(players_ratings_label, conn, player_name):
  player_names_df = sql_to_dataframe(conn, select_all_query_table("Player"))
  player_join_df = pd.merge(players_ratings_label, player_names_df, on='player_api_id', how='outer')
  COLUMNS_OF_INTEREST = ['player_name', 'finishing', 'sliding_tackle', 'gk_reflexes']
  my_player_df = (player_join_df[player_join_df['player_name'].str.contains(player_name)])
  most_recent_date = my_player_df['date'].max()
  return (my_player_df[my_player_df['date']==most_recent_date])[COLUMNS_OF_INTEREST]

if __name__ == '__main__':
  conn = uncompress_and_open_sqlite()
  matches_df = sql_to_dataframe(conn, select_all_query_table("Match"))
  home_advantage(matches_df=matches_df, conn = conn)