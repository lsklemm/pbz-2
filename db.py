import psycopg2

con = psycopg2.connect(
    host="localhost",
    port=5432,
    database="test2",
    user="postgres",
    password="stefa14065"
)
cur = con.cursor()