import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = BASE_DIR / "database" / "brauerei.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()

        # Tabelle für ESP32-Daten
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

        # Tabelle für Tilt-Hydrometer-Daten
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tilt_messungen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zeit TEXT UNIQUE,
            sg REAL,
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

    def speichern_tilt(self, zeit, sg, temperatur):

        self.cursor.execute("""
        INSERT OR IGNORE INTO tilt_messungen
        (zeit, sg, temperatur)
        VALUES (?, ?, ?)
        """,
        (
            zeit,
            sg,
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

    def lese_tilt_messungen(self):

        self.cursor.execute("""
        SELECT *
        FROM tilt_messungen
        ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    def schliessen(self):

        self.conn.close()