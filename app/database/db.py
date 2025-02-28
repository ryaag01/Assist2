# app/database/db.py
import sqlite3
from app.config import DATABASE_URL

def get_db_connection():
    # For SQLite, DATABASE_URL is in the format sqlite:///./assist.db
    db_path = DATABASE_URL.split("///")[-1]
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sample_table")  # Make sure this table exists
    data = cursor.fetchall()
    conn.close()
    return [dict(row) for row in data]
