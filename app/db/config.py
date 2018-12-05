import psycopg2
# import os

connect_url = "dbname='ireporter' host='localhost' port='5432' user='user' password=''"

def connect_db():
  '''Connect to database'''
  try:
      return psycopg2.connect(connect_url)
  except:
      print ("Unable to establish connection to database")

# returns connection for base db
def init_db():
    conn = connect_db()
    return conn

