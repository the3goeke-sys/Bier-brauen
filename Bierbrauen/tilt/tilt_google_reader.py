import pandas as pd
import re


class TiltGoogleReader:

    def __init__(self):

        self.sheet_url = "https://docs.google.com/spreadsheets/d/1KEggKynejpm6gIJTs4ZhCwXyKkE8BN2dEDOO1Z4JNMw/edit?usp=sharing"

    def _csv_url_erstellen(self):

        sheet_id_match = re.search(
            r"/spreadsheets/d/([a-zA-Z0-9-_]+)",
            self.sheet_url
        )

        if sheet_id_match is None:
            raise ValueError("Google-Sheets-Link ist ungültig.")

        sheet_id = sheet_id_match.group(1)

        gid_match = re.search(r"gid=([0-9]+)", self.sheet_url)
        gid = gid_match.group(1) if gid_match else "0"

        return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    def lese_daten(self):

        csv_url = self._csv_url_erstellen()

        df = pd.read_csv(csv_url)

        # Spaltennamen bereinigen
        df.columns = [str(col).strip() for col in df.columns]

        print("Gefundene Spalten:", list(df.columns))

        # passende Spalten finden
        time_col = "Timepoint"
        sg_col = "SG"

        temp_col = None
        for col in df.columns:
            if "Temp" in col:
                temp_col = col
                break

        if temp_col is None:
            raise ValueError("Keine Temperatur-Spalte gefunden.")

        daten = []

        for _, row in df.iterrows():

            try:
                zeit = row[time_col]
                sg = float(row[sg_col])
                temperatur_f = float(row[temp_col])
                temperatur = (temperatur_f - 32) * 5 / 9

                daten.append({
                    "zeit": str(zeit),
                    "sg": sg,
                    "temperatur": temperatur
                })

            except Exception as e:
                print("Zeile übersprungen:", e)

        return daten