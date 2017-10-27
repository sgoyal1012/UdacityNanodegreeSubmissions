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


def select_all_query_table(table_name):
  return "SELECT * from " + table_name