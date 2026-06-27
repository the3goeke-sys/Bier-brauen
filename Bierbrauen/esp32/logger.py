import time
import sys
from pathlib import Path

# Hauptordner finden, damit Imports funktionieren
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from database.database import Database
from esp32.serial_reader import SerialReader


# ---------------- OBJEKTE ERSTELLEN ----------------

serial_reader = SerialReader()
db = Database()

print("🍺 ESP32-Logger gestartet...")


# ---------------- HAUPTSCHLEIFE ----------------

while True:

    try:
        data = serial_reader.lese_daten()

        if data is None:
            continue

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

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

    except KeyboardInterrupt:
        print("ESP32-Logger beendet.")
        break

    except Exception as e:
        print("Fehler:", e)