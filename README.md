# Digitaler Zwilling für eine Bierbrauanlage

## Projektbeschreibung

Dieses Projekt implementiert einen digitalen Zwilling für eine Bierbrauanlage.

Die Messdaten werden mit einem ESP32 und verschiedenen Sensoren erfasst:

- Gewicht (NAU7802)
- Magnetfeld (TMAG5273)
- Temperatur

Die Daten werden:

- in einer SQLite-Datenbank gespeichert
- nach Google Sheets übertragen
- in einem Streamlit-Dashboard visualisiert

## Projektstruktur

```
ESP32_DASHBOARD/
│
├── app.py
├── logger.py
├── database
├── services
├── tests
```

## Start

Logger starten:

```
python logger.py
```

Dashboard starten:

```
streamlit run app.py
```
