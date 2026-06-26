import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleService:

    def __init__(self):

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            r"C:\Users\HP\Documents\esp32_dashboard\esp32-v2-dahboard-9f74cdd5d2c3.json",
            scope
        )

        client = gspread.authorize(creds)

        self.sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/16qSRsdqKqTuPO_ETw0Ee0vPv7hJxNWvxadl4e8w75mQ/edit?gid=0#gid=0"
        ).sheet1

    def speichern(self, zeit, gewicht, mx, my, mz, temperatur):

        self.sheet.append_row([
            zeit,
            gewicht,
            mx,
            my,
            mz,
            temperatur
        ])