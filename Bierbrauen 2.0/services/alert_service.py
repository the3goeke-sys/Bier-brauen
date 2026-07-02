class AlertService:

    def pruefe_alerts(self, temperatur, sg):
        alerts = []

        if temperatur > 24:
            alerts.append("Temperatur zu hoch.")

        if temperatur < 16:
            alerts.append("Temperatur zu niedrig.")

        if sg < 1.015:
            alerts.append("SG niedrig: Zuckergehalt wahrscheinlich stark gesunken.")

        return alerts