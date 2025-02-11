import streamlit as st
import numpy as np
import pandas as pd

# Definition der Parteien und Aussagen
parteien = ["Grüne", "Linke", "SPD", "CDU", "AfD", "FDP"]
aussagen = [
    "Schule & Bildung",
    "Umwelt & Klima",
    "Familie & Soziales",
    "Technik & Digitalisierung",
    "Freizeit & Verkehr",
    "Tiere & Umwelt",
    "Europa & Außenpolitik",
    "Geld & Wirtschaft",
    "Arbeit & Zukunft",
    "Migration & Flucht"
]

# Positionen der Parteien (3 = stark dafür, 2 = eher dafür, 1 = neutral, -2 = eher dagegen, -3 = stark dagegen)
positionen = np.array([
    [3,  3,  3,  3,  3,  3,  3,  3,  3,  3],  # Grüne
    [3,  3,  3,  3,  3,  3,  3,  3,  3,  3],  # Linke
    [2,  2,  2,  3,  2,  2,  3,  2,  2,  2],  # SPD
    [-2, -2, -2,  2, -2, -2,  2, -2, -2, -2],  # CDU
    [-3, -3, -3, -2, -3, -3, -3, -3, -3, -3],  # AfD
    [-2, -2, -2,  2, -2, -2,  2, -2, -2, -2],  # FDP
])

# Streamlit App
st.title("Dein Wahl-Tool für Kinder")
st.write("Beantworte die Fragen und finde heraus, welche Partei am besten zu dir passt!")

# Nutzerantworten speichern
nutzer_antworten = []

for i, aussage in enumerate(aussagen):
    antwort = st.radio(
        f"{aussage}",
        ("Stimme voll zu", "Stimme eher zu", "Neutral", "Stimme eher nicht zu", "Stimme gar nicht zu"),
        index=2
    )
    
    # Antwort in Zahlenwert umwandeln
    antwort_wert = {
        "Stimme voll zu": 3,
        "Stimme eher zu": 2,
        "Neutral": 1,
        "Stimme eher nicht zu": -2,
        "Stimme gar nicht zu": -3
    }[antwort]
    
    nutzer_antworten.append(antwort_wert)

# Ergebnisse berechnen, wenn Button gedrückt wird
if st.button("Ergebnis anzeigen"):
    partei_scores = np.dot(positionen, nutzer_antworten)
    ergebnis_df = pd.DataFrame({"Partei": parteien, "Übereinstimmung": partei_scores})
    ergebnis_df = ergebnis_df.sort_values(by="Übereinstimmung", ascending=False)
    
    st.subheader("Deine beste Übereinstimmung:")
    st.write(ergebnis_df)
    st.bar_chart(ergebnis_df.set_index("Partei"))
