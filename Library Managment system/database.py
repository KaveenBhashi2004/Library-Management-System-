
from contextlib import contextmanager
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("library.db")


@contextmanager
def connect_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def create_database():
    with connect_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS fines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                email TEXT NOT NULL,
                book_name TEXT NOT NULL,
                overdue_days INTEGER NOT NULL,
                raw_fine REAL NOT NULL,
                fine REAL NOT NULL,
                status TEXT NOT NULL,
                membership TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_record(name, email, book, days,
                raw, fine, status, membership):

    with connect_db() as db:
        cursor = db.execute("""
            INSERT INTO fines (
                student_name, email, book_name,
                overdue_days, raw_fine, fine,
                status, membership
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, email, book, days,
            raw, fine, status, membership
        ))
        return cursor.lastrowid


def get_records():
    with connect_db() as db:
        records = db.execute("""
            SELECT * FROM fines
            ORDER BY id DESC
        """).fetchall()

    return records


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
