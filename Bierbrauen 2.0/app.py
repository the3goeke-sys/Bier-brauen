import streamlit as st
from controller.dashboard_controller import DashboardController

st.set_page_config(
    page_title="Digitaler Zwilling Brauanlage",
    layout="wide"
)

st.title("🍺 Digitaler Zwilling Brauanlage")

controller = DashboardController()

df_esp32 = controller.get_esp32_daten()
df_tilt = controller.get_tilt_daten()

st.header("📟 ESP32 Sensordaten")

if df_esp32.empty:
    st.warning("Noch keine ESP32-Daten vorhanden.")
else:
    aktuelle_esp32 = df_esp32.iloc[0]
    temperatur = float(aktuelle_esp32["temperatur"])
    gewicht = float(aktuelle_esp32["gewicht"])

    gaerstatus = controller.get_gaerstatus(temperatur)

    col1, col2, col3 = st.columns(3)

    col1.metric("Gewicht", f"{gewicht:.2f} kg")
    col2.metric("ESP32 Temperatur", f"{temperatur:.1f} °C")
    col3.metric("Gärstatus", gaerstatus)

    st.dataframe(df_esp32, use_container_width=True)

st.divider()

st.header("🍺 Tilt Hydrometer Daten")

if df_tilt.empty:
    st.warning("Noch keine Tilt-Daten vorhanden.")
else:
    aktuelle_tilt = df_tilt.iloc[0]
    sg = float(aktuelle_tilt["sg"])
    tilt_temp = float(aktuelle_tilt["temperatur"])

    col4, col5 = st.columns(2)

    col4.metric("Aktuelle Dichte / SG", f"{sg:.3f}")
    col5.metric("Tilt Temperatur", f"{tilt_temp:.1f} °C")

    alerts = controller.get_alerts(tilt_temp, sg)

    for alert in alerts:
        st.warning(alert)

    st.dataframe(df_tilt, use_container_width=True)