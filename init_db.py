import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL,
        photo TEXT NOT NULL,
        comment TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO people (name, birthday, photo, comment)
    VALUES ('홍길동', '2000-01-01', 'hong.jpg', '홍길동입니다.')
    """)

    conn.commit()
    conn.close()

init_db()