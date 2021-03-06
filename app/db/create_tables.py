from app.db.config import open_connection, open_testDb_connection, close_connection

QUERIES = [
  """
  CREATE TABLE IF NOT EXISTS users(
          id SERIAL PRIMARY KEY NOT NULL,
          firstname VARCHAR NOT NULL,
          lastname VARCHAR NOT NULL,
          othernames VARCHAR NOT NULL,
          email VARCHAR NOT NULL,
          phoneNumber VARCHAR NOT NULL,
          username VARCHAR NOT NULL,
          password VARCHAR NOT NULL,
          registered TIMESTAMP,
          isAdmin BOOLEAN
          )
  """,

  """
  CREATE TABLE IF NOT EXISTS incidents(
          id SERIAL PRIMARY KEY NOT NULL,
          createdOn TIMESTAMP,
          createdBy INT REFERENCES users(id),
          type VARCHAR NOT NULL,
          location VARCHAR NOT NULL,
          status VARCHAR NOT NULL,
          Images VARCHAR[] NOT NULL,
          Videos VARCHAR[] NOT NULL,
          comment VARCHAR NOT NULL
          )
  """
]

queries = [
    'DROP table users CASCADE',
    'DROP table incidents CASCADE'
]


def create_tables():
    #create tables for base db
    conn = open_connection()
    cur = conn.cursor()

    for query in QUERIES:
        cur.execute(query)

    close_connection(conn)


def create_test_tables():
    #create tables for test db
    conn = open_testDb_connection()
    cur = conn.cursor()

    for query in QUERIES:
        cur.execute(query)

    close_connection(conn)


def drop_tables():
    #dropping base db tables
    conn = open_connection()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)

    cur.close()
    conn.commit()


def drop_test_tables():
    #dropping test db tables
    conn = open_testDb_connection()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)

    cur.close()
    conn.commit()