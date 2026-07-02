# Messung der Ladezeit
# Gemessen wurde die Zeit, die das Dashboard benötigt,
# um die Messwerte aus der SQLite-Datenbank zu laden
# und für die Anzeige vorzubereiten.


import sqlite3
import time
import statistics
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "brauerei.db"

ANZAHL_MESSUNGEN = 100

messwerte = []

for i in range(ANZAHL_MESSUNGEN):
    start = time.perf_counter()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM messungen
    ORDER BY id DESC
    LIMIT 100
    """)
    esp32_daten = cursor.fetchall()

    cursor.execute("""
    SELECT *
    FROM tilt_messungen
    ORDER BY id DESC
    LIMIT 100
    """)
    tilt_daten = cursor.fetchall()

    conn.close()

    ende = time.perf_counter()

    ladezeit_ms = (ende - start) * 1000
    messwerte.append(ladezeit_ms)

    print(f"Messung {i + 1}: {ladezeit_ms:.2f} ms")


mittelwert = statistics.mean(messwerte)
median = statistics.median(messwerte)
standardabweichung = statistics.stdev(messwerte)
minimum = min(messwerte)
maximum = max(messwerte)

print("\n EInmal hier die Auswertung der Ladezeiten:")
print(f"Anzahl Messungen: {ANZAHL_MESSUNGEN}")
print(f"Minimum: {minimum:.2f} ms")
print(f"Maximum: {maximum:.2f} ms")
print(f"Mittelwert: {mittelwert:.2f} ms")
print(f"Median: {median:.2f} ms")
print(f"Standardabweichung: {standardabweichung:.2f} ms")
print(f"ESP32-Datensätze geladen: {len(esp32_daten)}")
print(f"Tilt-Datensätze geladen: {len(tilt_daten)}")