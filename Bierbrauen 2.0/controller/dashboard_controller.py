import pandas as pd
from database.database import Database
from services.fermentation_service import FermentationService
from services.alert_service import AlertService


class DashboardController:

    def __init__(self):
        self.db = Database()
        self.fermentation_service = FermentationService()
        self.alert_service = AlertService()

    def get_esp32_daten(self):
        daten = self.db.lese_messungen()
        return pd.DataFrame(
            daten,
            columns=["id", "zeit", "gewicht", "mx", "my", "mz", "temperatur"]
        )

    def get_tilt_daten(self):
        daten = self.db.lese_tilt_messungen()
        return pd.DataFrame(
            daten,
            columns=["id", "zeit", "sg", "temperatur"]
        )

    def get_gaerstatus(self, temperatur):
        return self.fermentation_service.bewerte_temperatur(temperatur)

    def get_alerts(self, temperatur, sg):
        return self.alert_service.pruefe_alerts(temperatur, sg)