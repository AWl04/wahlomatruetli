import streamlit as st
import numpy as np
import pandas as pd

# Definition der Parteien und Aussagen
parteien = ["Grüne", "Linke", "SPD", "CDU", "AfD", "FDP"]
aussagen = [
    "Alle Kinder sollen so lange wie möglich auf eine Schule gehen können, wo mehrere Abschlüsse möglich sind.",
    "Autos sollen weniger Abgase ausstoßen, auch wenn das teurer wird.",
    "Eltern sollen mehr Geld vom Staat bekommen, damit sie sich besser um ihre Kinder kümmern können.",
    "In allen Schulen soll es kostenloses WLAN und moderne Computer geben.",
    "Busse und Bahnen sollen für Kinder und Jugendliche kostenlos sein.",
    "Es soll strengere Regeln geben, damit Bauern ihre Tiere besser behandeln müssen.",
    "Deutschland soll helfen, wenn andere Länder in Not sind.",
    "Menschen, die viel Geld verdienen, sollen mehr Steuern zahlen als andere.",
    "Alle Menschen sollen so arbeiten können, dass sie genug Geld zum Leben haben, ohne sich Sorgen machen zu müssen.",
    "Alle Menschen, die in Deutschland Schutz suchen, sollen einen Asylantrag stellen können."
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
