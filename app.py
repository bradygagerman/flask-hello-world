import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Brady Gagerman in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10_postgres_user:GvvbszQR9ly9v84DtFJatoIoq1T3bdKU@dpg-cqhcj5d6l47c73flo800-a/lab10_postgres")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://lab10_postgres_user:GvvbszQR9ly9v84DtFJatoIoq1T3bdKU@dpg-cqhcj5d6l47c73flo800-a/lab10_postgres")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfullt Created"