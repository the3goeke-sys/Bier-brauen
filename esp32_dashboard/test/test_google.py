from services.google_service import GoogleService

google = GoogleService()

google.speichern(
    "2026-06-26 12:00:00",
    3.25,
    1.2,
    0.8,
    0.5,
    21.5
)

print("Testeintrag erfolgreich in Google Sheets gespeichert.")