# Messung der Ladezeit
# Gemessen wird die Zeit, die das Dashboard benötigt,
# um die ESP32- und Tilt-Daten über den DashboardController
# aus der SQLite-Datenbank zu laden und für die Anzeige vorzubereiten.

import time
import statistics
import csv
from controller.dashboard_controller import DashboardController


ANZAHL_MESSUNGEN = 100
messwerte = []

print("Messung der Ladezeit für das Dashboard")
print("Gemessen wird der Datenabruf über den DashboardController.")
print()

for i in range(ANZAHL_MESSUNGEN):
    start = time.perf_counter()

    controller = DashboardController()

    df_esp32 = controller.get_esp32_daten()
    df_tilt = controller.get_tilt_daten()

    ende = time.perf_counter()

    ladezeit_ms = (ende - start) * 1000
    messwerte.append(ladezeit_ms)

    print(f"Messung {i + 1}: {ladezeit_ms:.2f} ms")


mittelwert = statistics.mean(messwerte)
median = statistics.median(messwerte)
standardabweichung = statistics.stdev(messwerte)
minimum = min(messwerte)
maximum = max(messwerte)

print()
print("--- Auswertung ---")
print(f"Anzahl der Messungen: {ANZAHL_MESSUNGEN}")
print(f"Minimum: {minimum:.2f} ms")
print(f"Maximum: {maximum:.2f} ms")
print(f"Mittelwert: {mittelwert:.2f} ms")
print(f"Median: {median:.2f} ms")
print(f"Standardabweichung: {standardabweichung:.2f} ms")
print(f"ESP32-Datensätze geladen: {len(df_esp32)}")
print(f"Tilt-Datensätze geladen: {len(df_tilt)}")
