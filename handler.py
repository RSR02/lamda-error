import json



DB_HOST = "database-1.ca4aq03flcwk.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "QTvHKaPlSw6WGeiOIJWj"

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

        cur.execute("SELECT * FROM examp;")
        print(cur.fetchall())
conn.close()
#hello
