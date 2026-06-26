import sqlite3

DB_NAME = "database/brauerei.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS messungen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zeit TEXT,
            gewicht REAL,
            mx REAL,
            my REAL,
            mz REAL,
            temperatur REAL
        )
        """)

        self.conn.commit()

    def speichern(self, zeit, gewicht, mx, my, mz, temperatur):

        self.cursor.execute("""
        INSERT INTO messungen
        (zeit, gewicht, mx, my, mz, temperatur)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            zeit,
            gewicht,
            mx,
            my,
            mz,
            temperatur
        ))

        self.conn.commit()

    def lese_messungen(self):

        self.cursor.execute("""
        SELECT *
        FROM messungen
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def schliessen(self):

        self.conn.close()