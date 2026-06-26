import streamlit as st
import pandas as pd
import sqlite3

# ---------------- Einstellungen ----------------

st.set_page_config(
    page_title="Digitaler Zwilling Brauanlage",
    layout="wide"
)

st.title("🍺 Digitaler Zwilling Brauanlage")

# ---------------- Datenbank ----------------

conn = sqlite3.connect("database/brauerei.db")

df = pd.read_sql_query("""
SELECT *
FROM messungen
ORDER BY id DESC
LIMIT 500
""", conn)

conn.close()

# ---------------- Dashboard ----------------

if df.empty:
    st.warning("Noch keine Daten vorhanden.")

else:

    df = df.sort_values("id")

    # Aktuelle Werte
    aktuelles_gewicht = float(df["gewicht"].iloc[-1])
    aktuelle_temp = float(df["temperatur"].iloc[-1])

    # Gärstatus bestimmen
    if 20 <= aktuelle_temp <= 22:
        gaerstatus = "🟢 Optimal"

    elif 18 <= aktuelle_temp < 20 or 22 < aktuelle_temp <= 25:
        gaerstatus = "🟡 Beobachten"

    else:
        gaerstatus = "🔴 Kritisch"

    # Kennzahlen
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "⚖️ Gewicht",
            f"{aktuelles_gewicht:.2f} kg"
        )

    with col2:
        st.metric(
            "🌡️ Temperatur",
            f"{aktuelle_temp:.1f} °C"
        )

    with col3:
        st.metric(
            "🍺 Gärstatus",
            gaerstatus
        )

    st.divider()

    # Gewichtsdiagramm
    st.subheader("⚖️ Gewichtsverlauf")

    st.line_chart(
        df.set_index("zeit")["gewicht"]
    )

    # Temperaturdiagramm
    st.subheader("🌡️ Temperaturverlauf")

    st.line_chart(
        df.set_index("zeit")["temperatur"]
    )

    st.divider()

    # Letzte Messungen
    st.subheader("📋 Letzte 100 Messungen")

    st.dataframe(
        df.tail(100),
        use_container_width=True
    )