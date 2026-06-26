from services.serial_reader import SerialReader

reader = SerialReader()

print("Teste serielle Verbindung...")

while True:

    daten = reader.lese_daten()

    if daten is not None:
        print(daten)