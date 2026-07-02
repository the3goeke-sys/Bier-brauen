class FermentationService:

    def bewerte_temperatur(self, temperatur):
        if 20 <= temperatur <= 22:
            return "🟢 Optimal"
        elif 18 <= temperatur < 20 or 22 < temperatur <= 25:
            return "🟡 Beobachten"
        else:
            return "🔴 Kritisch"

    def bewerte_sg(self, sg):
        if sg <= 1.015:
            return "Gärung vermutlich weit fortgeschritten"
        elif sg <= 1.025:
            return "Gärung läuft noch"
        else:
            return "Gärung aktiv / hoher Zuckergehalt"