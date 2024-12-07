import sqlite3
from sqlite3 import Error

def create_connection():
    """Creates a database connection to the SQLite database."""
    try:
        conn = sqlite3.connect('weather.db')
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    """Creates the 'daily_summaries' table if it doesn't exist."""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS daily_summaries (
                    city TEXT NOT NULL,
                    date TEXT NOT NULL,
                    avg_temp REAL NOT NULL,
                    max_temp REAL NOT NULL,
                    min_temp REAL NOT NULL,
                    weather_condition TEXT NOT NULL,
                    UNIQUE(city, date)
                )
            ''')
            conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

def fetch_daily_summaries():
    """Fetches all daily summaries from the 'daily_summaries' table."""
    summaries = []
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM daily_summaries')
            rows = cursor.fetchall()

            summaries = [
                {
                    'city': row[0],
                    'date': row[1],
                    'avg_temp': row[2],
                    'max_temp': row[3],
                    'min_temp': row[4],
                    'weather_condition': row[5]
                }
                for row in rows
            ]
        except Error as e:
            print(f"Error fetching data: {e}")
        finally:
            conn.close()
    return summaries

def insert_daily_summary(city, date, avg_temp, max_temp, min_temp, weather_condition):
    """Inserts a daily weather summary into the 'daily_summaries' table."""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO daily_summaries (city, date, avg_temp, max_temp, min_temp, weather_condition)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (city, date, avg_temp, max_temp, min_temp, weather_condition))
            conn.commit()
        except Error as e:
            print(f"Error inserting data: {e}")
        finally:
            conn.close()












