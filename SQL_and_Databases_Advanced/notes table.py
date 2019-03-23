

import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE notes(id integer primary key, body text, title text)")
conn.close()

