'''
FORMATTING CONSTANTS
'''
SEPARATOR = "***********************************************"

'''

'''

'''
INPUT DATA Constants
'''
INPUTFILE_DIR = "../Data/"
INPUTZIPFILE = "soccer.zip"
DATABASENAME = "database.sqlite"

'''
SQL STATEMENTS
'''
SHOW_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type='table' " \
                  "ORDER BY name;"
DESC_TABLES_SQL = "DESC"

import pandas as pd

def select_all_query_table(table_name):
  return "SELECT * from " + table_name

def sql_to_dataframe(conn, sql):
  df = pd.read_sql_query(sql, conn)
  return df


def map_country_to_name(countries_df, country_id):
  return countries_df.loc[countries_df['id'] == country_id, 'name']