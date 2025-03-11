from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="flaskdb",
        user="flaskuser",
        password="postgres",
        host="postgres"
    )
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    conn.close()
    return "Flask App Connected to PostgreSQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

