import gspread
import serial
import time
from oauth2client.service_account import ServiceAccountCredentials

# ---------------- GOOGLE SHEETS ----------------

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\HP\Documents\esp32_dashboard\esp32-v2-dahboard-9f74cdd5d2c3.json",
    scope
)

client = gspread.authorize(creds)

sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/16qSRsdqKqTuPO_ETw0Ee0vPv7hJxNWvxadl4e8w75mQ/edit?gid=0#gid=0"
).sheet1

# ---------------- SERIELL ----------------

ser = serial.Serial("COM9", 115200)

time.sleep(2)

print("System gestartet...")

while True:

    try:

        line = ser.readline().decode("utf-8").strip()

        if not line:
            continue

        print("Empfangen:", line)

        data = line.split(",")

        # Jetzt 5 Werte prüfen
        if len(data) != 5:
            print("Ungültige Daten:", line)
            continue

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        sheet.append_row([
            timestamp,  # Zeit
            data[0],    # Gewicht kg
            data[1],    # MX
            data[2],    # MY
            data[3],    # MZ
            data[4]     # Temperatur °C
        ])

        print("OK:", data)

    except Exception as e:
        print("Fehler:", e)

import sys
print(sys.executable)