import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path


# ---------------- Einstellungen ----------------

st.set_page_config(
    page_title="Digitaler Zwilling Brauanlage",
    layout="wide"
)

st.title("🍺 Digitaler Zwilling Brauanlage")


# ---------------- Datenbank-Pfad ----------------

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "brauerei.db"


# ---------------- Datenbank vorbereiten ----------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zeit TEXT,
    gewicht REAL,
    mx REAL,
    my REAL,
    mz REAL,
    temperatur REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tilt_messungen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zeit TEXT UNIQUE,
    sg REAL,
    temperatur REAL
)
""")

conn.commit()


# ---------------- Daten laden ----------------

df_esp32 = pd.read_sql_query("""
SELECT *
FROM messungen
ORDER BY id DESC
LIMIT 100
""", conn)

df_tilt = pd.read_sql_query("""
SELECT *
FROM tilt_messungen
ORDER BY id DESC
LIMIT 100
""", conn)

conn.close()


# ---------------- ESP32 Dashboard ----------------

st.header("📟 ESP32 Sensordaten")

if df_esp32.empty:
    st.warning("Noch keine ESP32-Daten vorhanden.")

else:
    df_esp32["gewicht"] = pd.to_numeric(df_esp32["gewicht"], errors="coerce")
    df_esp32["temperatur"] = pd.to_numeric(df_esp32["temperatur"], errors="coerce")

    df_esp32 = df_esp32.dropna(subset=["gewicht", "temperatur"])

    if df_esp32.empty:
        st.warning("ESP32-Daten konnten nicht korrekt gelesen werden.")

    else:
        aktuelle_esp32 = df_esp32.iloc[0]

        aktuelles_gewicht = float(aktuelle_esp32["gewicht"])
        aktuelle_temp = float(aktuelle_esp32["temperatur"])

        if 20 <= aktuelle_temp <= 22:
            gaerstatus = "🟢 Optimal"
        elif 18 <= aktuelle_temp < 20 or 22 < aktuelle_temp <= 25:
            gaerstatus = "🟡 Beobachten"
        else:
            gaerstatus = "🔴 Kritisch"

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("⚖️ Gewicht", f"{aktuelles_gewicht:.2f} kg")

        with col2:
            st.metric("🌡️ ESP32 Temperatur", f"{aktuelle_temp:.1f} °C")

        with col3:
            st.metric("🍺 Gärstatus", gaerstatus)

        st.subheader("📋 Letzte ESP32-Messungen")

        st.dataframe(
            df_esp32,
            use_container_width=True
        )


# ---------------- Tilt Hydrometer Dashboard ----------------

st.divider()

st.header("🍺 Tilt Hydrometer Daten")

if df_tilt.empty:
    st.warning("Noch keine Tilt-Hydrometer-Daten vorhanden.")

else:
    df_tilt["sg"] = pd.to_numeric(df_tilt["sg"], errors="coerce")
    df_tilt["temperatur"] = pd.to_numeric(df_tilt["temperatur"], errors="coerce")

    df_tilt = df_tilt.dropna(subset=["sg", "temperatur"])

    if df_tilt.empty:
        st.warning("Tilt-Daten konnten nicht korrekt gelesen werden.")

    else:
        aktuelle_tilt = df_tilt.iloc[0]

        aktuelle_sg = float(aktuelle_tilt["sg"])
        aktuelle_tilt_temp = float(aktuelle_tilt["temperatur"])

        col4, col5 = st.columns(2)

        with col4:
            st.metric("🍺 Aktuelle Dichte / SG", f"{aktuelle_sg:.3f}")

        with col5:
            st.metric("🌡️ Tilt Temperatur", f"{aktuelle_tilt_temp:.1f} °C")

        st.subheader("📋 Letzte Tilt-Messungen")

        st.dataframe(
            df_tilt,
            use_container_width=True
        )