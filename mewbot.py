import pickle
import psycopg2
import os
dburl = os.environ['DATABASE_URL']
conn = psycopg2.connect(dburl)

with conn.cursor() as cur:
    cur.execute('SELECT * FROM pokes;')
    rows = cur.fetch()

with open('file.pickle', 'w') as fp:
    pickle.dump(rows, fp)
