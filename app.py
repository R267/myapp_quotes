from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Параметри підключення до БД з змінних середовища
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "quotes_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

# Функція отримання цитати з БД
def get_random_quote():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT text FROM quotes ORDER BY RANDOM() LIMIT 1;")
        quote = cur.fetchone()
        conn.close()
        return quote[0] if quote else "No quotes found."
    except Exception as e:
        return f"Database error: {e}"

@app.route("/quote")
def quote():
    return jsonify({"quote": get_random_quote()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
