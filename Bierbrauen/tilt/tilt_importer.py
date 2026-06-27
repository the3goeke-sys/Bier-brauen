import time
import sys
from pathlib import Path

# Damit Python auch den Hauptordner findet
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from database.database import Database
from tilt.tilt_google_reader import TiltGoogleReader


reader = TiltGoogleReader()
db = Database()

print("🍺 Tilt-Importer gestartet...")


while True:

    try:
        daten = reader.lese_daten()

        for messung in daten:

            db.speichern_tilt(
                messung["zeit"],
                messung["sg"],
                messung["temperatur"]
            )

        print(f"OK | {len(daten)} Tilt-Zeilen geprüft")

    except Exception as e:
        print("Fehler beim Tilt-Import:", e)

    # alle 5 Minuten prüfen
    time.sleep(300)