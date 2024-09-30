import psycopg2 as pg2


DB_URL = '127.0.0.1'
DB = 'scas'
User = 'augustine77'
PW = '!8366hug@#'
Port = '5432'
pg_conn = pg2.connect(f"host={DB_URL} dbname={DB} user={User} password={PW} port={Port}")

query = "CREATE TABLE testTB (id SERIAL PRIMARY KEY, name VARCHAR(10));"

with pg_conn.cursor() as curr:
    curr.execute(query)

pg_conn.commit()
pg_conn.close()
