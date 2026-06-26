import time

from database.database import Database
from services.serial_reader import SerialReader
from services.google_service import GoogleService

# ---------------- OBJEKTE ERSTELLEN ----------------

serial_reader = SerialReader()
google = GoogleService()
db = Database()

print("🍺 Logger gestartet...")

# ---------------- HAUPTSCHLEIFE ----------------

while True:

    try:

        data = serial_reader.lese_daten()

        if data is None:
            continue

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # ---------------- GOOGLE SHEETS ----------------

        google.speichern(
            timestamp,
            data["gewicht"],
            data["mx"],
            data["my"],
            data["mz"],
            data["temperatur"]
        )

        # ---------------- SQLITE ----------------

        db.speichern(
            timestamp,
            data["gewicht"],
            data["mx"],
            data["my"],
            data["mz"],
            data["temperatur"]
        )

        print(
            f"OK | Gewicht={data['gewicht']:.2f} kg | "
            f"Temp={data['temperatur']:.1f} °C"
        )

    except Exception as e:
        print("Fehler:", e)