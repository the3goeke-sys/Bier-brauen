from database.database import Database

db = Database()

db.speichern(
    "2026-06-26 12:00:00",
    3.25,
    1.2,
    0.8,
    0.5,
    21.5
)

daten = db.lese_messungen()

print("Letzter Datenbankeintrag:")
print(daten[0])

db.schliessen()