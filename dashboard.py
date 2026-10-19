

import streamlit as st
import pandas as pd
from pathlib import Path

# Dashboard konfigurieren
st.set_page_config(
    page_title="Cloud Machine Monitoring",
    layout="wide"
)

st.title("Cloud Machine Monitoring")
st.write("Ueberwachung simulierter Maschinendaten")

# CSV-Datei im gleichen Ordner suchen
dateipfad = Path(__file__).with_name("maschinendaten.csv")

if not dateipfad.exists():
    st.error("Keine CSV-Datei gefunden!")
    st.write("Bitte zuerst simulierte_daten.py ausfuehren.")

else:
    daten = pd.read_csv(dateipfad)

    # Kennzahlen berechnen
    grenzwert = 90
    anzahl_messungen = len(daten)
    durchschnitt = daten["Messwert"].mean()
    max_wert = daten["Messwert"].max()
    warnungen = daten[daten["Messwert"] > grenzwert]

    # Kennzahlen oben anzeigen
    spalte1, spalte2, spalte3, spalte4 = st.columns(4)

    spalte1.metric("Messungen", anzahl_messungen)
    spalte2.metric("Durchschnitt", f"{durchschnitt:.2f}")
    spalte3.metric("Maximalwert", f"{max_wert:.2f}")
    spalte4.metric("Warnungen", len(warnungen))

    # Diagramm
    st.subheader("Messwerte im Verlauf")
    daten["Messung"] = range(1, len(daten) + 1)

    st.line_chart(
        daten.set_index("Messung")["Messwert"],
        height=400   # Diagrammhoehe in Pixeln festlegen
    )

    # Warnmeldungen
    st.subheader("Grenzwertueberwachung")

    if len(warnungen) > 0:
        st.warning(
            f"{len(warnungen)} Messwerte ueberschreiten den Grenzwert von 90."
        )
        st.dataframe(warnungen, use_container_width=True)
    else:
        st.success("Keine Grenzwertueberschreitungen festgestellt.")
    # Alle Daten optional anzeigen
    with st.expander("Alle Messdaten anzeigen"):
        st.dataframe(daten, use_container_width=True)
