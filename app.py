import streamlit as st
import numpy as np
import pandas as pd

# Definition der Parteien und Aussagen
parteien = ["Grüne", "Linke", "SPD", "CDU", "AfD", "FDP"]
aussagen = [
    "1. Alle Kinder sollen so lange wie möglich auf eine Schule gehen können, wo mehrere Abschlüsse möglich sind.",
    "2. Autos sollen weniger Abgase ausstoßen, auch wenn das teurer wird.",
    "3. Eltern sollen mehr Geld vom Staat bekommen, damit sie sich besser um ihre Kinder kümmern können.",
    "4. In allen Schulen soll es kostenloses WLAN und moderne Computer geben.",
    "5. Busse und Bahnen sollen für Kinder und Jugendliche kostenlos sein.",
    "6. Es soll strengere Regeln geben, damit Bauern ihre Tiere besser behandeln müssen.",
    "7. Deutschland soll helfen, wenn andere Länder in Not sind.",
    "8. Menschen, die viel Geld verdienen, sollen mehr Steuern zahlen als andere.",
    "9. Alle Menschen sollen so arbeiten können, dass sie genug Geld zum Leben haben, ohne sich Sorgen machen zu müssen.",
    "10. Alle Menschen, die in Deutschland Schutz suchen, sollen einen Asylantrag stellen können."
]

# Meinungen der Parteien zu den Aussagen
meinungen = {
    "Grüne": ["Ja, wir unterstützen das!", "Ja, wichtig für den Klimaschutz!", "Ja, Familien müssen unterstützt werden!", "Ja, Digitalisierung ist entscheidend!", "Ja, kostenloser Nahverkehr hilft allen!", "Ja, mehr Tierschutz ist nötig!", "Ja, wir müssen helfen!", "Ja, soziale Gerechtigkeit ist wichtig!", "Ja, faire Löhne für alle!", "Ja, Asylrecht muss gewahrt bleiben!"],
    "Linke": ["Ja, alle sollen gleiche Chancen haben!", "Ja, Klimaschutz geht vor!", "Ja, Reiche sollen mehr zahlen!", "Ja, Bildung muss kostenlos sein!", "Ja, Mobilität ist ein Grundrecht!", "Ja, Tierschutz ist eine Priorität!", "Ja, wir helfen solidarisch!", "Ja, Reiche sollen mehr beitragen!", "Ja, gute Arbeit für alle!", "Ja, keine Abschiebungen mehr!"],
    "SPD": ["Ja, aber mit Kompromissen!", "Ja, aber nicht zu schnell!", "Ja, aber wir müssen es finanzieren!", "Ja, aber Schulen müssen mitmachen!", "Ja, aber nur für Bedürftige!", "Ja, aber mit Unterstützung für Bauern!", "Ja, aber mit EU-Abstimmung!", "Ja, aber mit Augenmaß!", "Ja, aber auch Unternehmen müssen profitieren!", "Ja, aber kontrollierte Migration!"],
    "CDU": ["Nein, wir brauchen unterschiedliche Schulen!", "Nein, zu teuer für Autofahrer!", "Nein, Familien sollen selbst vorsorgen!", "Ja, aber nicht als Pflicht!", "Nein, das kostet zu viel!", "Nein, Bauern sollten selbst entscheiden!", "Ja, aber nur begrenzt!", "Nein, zu hohe Steuern schaden der Wirtschaft!", "Nein, der Markt regelt das!", "Nein, Migration muss begrenzt werden!"],
    "AfD": ["Nein, das alte System funktioniert!", "Nein, Klimawandel ist nicht menschengemacht!", "Nein, weniger Staat, mehr Eigenverantwortung!", "Nein, Digitalisierung ist überbewertet!", "Nein, keine staatlichen Zuschüsse für Verkehr!", "Nein, Tierschutz ist überreguliert!", "Nein, wir sollen uns nicht einmischen!", "Nein, Steuern senken für alle!", "Nein, der Markt regelt Löhne!", "Nein, keine Aufnahme von Migranten!"],
    "FDP": ["Nein, Leistung muss sich lohnen!", "Nein, Technologie soll es lösen!", "Nein, keine zusätzlichen Ausgaben!", "Ja, aber mit privaten Anbietern!", "Nein, keine Gratisleistungen!", "Nein, Tierschutz über den Markt regeln!", "Ja, aber wirtschaftlich vertretbar!", "Nein, niedrige Steuern fördern Wachstum!", "Nein, Arbeitsmarkt muss flexibel bleiben!", "Nein, nur qualifizierte Migration!"]
}

# Positionen der Parteien (3 = stark dafür, 2 = eher dafür, 1 = neutral, -2 = eher dagegen, -3 = stark dagegen)
positionen = np.array([
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Grüne
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Linke
    [2, 2, 2, 3, 2, 2, 3, 2, 2, 2],  # SPD
    [-2, -2, -2, 2, -2, -2, 2, -2, -2, -2],  # CDU
    [-3, -3, -3, -2, -3, -3, -3, -3, -3, -3],  # AfD
    [-2, -2, -2, 2, -2, -2, 2, -2, -2, -2],  # FDP
])

# Streamlit App
st.title("Dein Wahl-Tool für Kinder")
st.write("Beantworte die Fragen und finde heraus, welche Partei am besten zu dir passt!")

nutzer_antworten = []
for i, aussage in enumerate(aussagen):
    antwort = st.radio(
        f"{aussage}",
        ("Stimme voll zu", "Stimme eher zu", "Neutral", "Stimme eher nicht zu", "Stimme gar nicht zu"),
        index=2
    )
    
    antwort_wert = {"Stimme voll zu": 3, "Stimme eher zu": 2, "Neutral": 1, "Stimme eher nicht zu": -2, "Stimme gar nicht zu": -3}[antwort]
    nutzer_antworten.append(antwort_wert)

if st.button("Ergebnis anzeigen"):
    partei_scores = np.dot(positionen, nutzer_antworten)
    ergebnis_df = pd.DataFrame({"Partei": parteien, "Übereinstimmung": partei_scores})
    ergebnis_df = ergebnis_df.sort_values(by="Übereinstimmung", ascending=False)
    
    st.subheader("Deine beste Übereinstimmung:")
    best_match = ergebnis_df.iloc[0]
    st.markdown(f"**{best_match['Partei']} passt am besten zu dir!**")
    
    for i, partei in enumerate(ergebnis_df["Partei"]):
        with st.expander(f"{partei} - {ergebnis_df['Übereinstimmung'].iloc[i]} Punkte"):
            for j, aussage in enumerate(aussagen):
                st.write(f"**{aussage}**: {meinungen[partei][j]}")
    
    st.bar_chart(ergebnis_df.set_index("Partei"))
