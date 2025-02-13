import streamlit as st
import numpy as np
import pandas as pd

# Definition der Parteien und Aussagen
parteien = ["Grüne", "Linke", "SPD", "CDU", "AfD", "FDP"]
aussagen = [
    "1. Alle Kinder sollen so lange wie möglich auf eine Schule gehen können, wo mehrere Abschlüsse möglich sind.",
    "2. Autos sollen weniger Abgase ausstoßen, auch wenn das teurer wird.",
    "3. Der Staat soll Eltern zusätzliches Geld geben, damit sie sich gut um ihre Kinder kümmern können.",
    "4. In allen Schulen soll es kostenloses WLAN und moderne Computer geben.",
    "5. Busse und Bahnen sollen für Kinder und Jugendliche kostenlos sein.",
    "6. Bauern sollen keine strengeren Regeln für die Tierhaltung bekommen, damit die Lebensmittelpreise niedrig bleiben.",
    "7. Der Ausbau von erneuerbaren Energien soll nicht vom Staat mit Geld unterstützt werden.",
    "8. Der Staat soll allen Menschen ein Grundeinkommen zahlen, auch wenn sie nicht arbeiten.",
    "9. Die Mietpreise sollen immer weiter erhöht werden dürfen, weil Vermieter frei entscheiden dürfen, wie viel sie verlangen.",
    "10. Alle Menschen, die in Deutschland Schutz suchen, sollen einen Asylantrag stellen können."
]

# Meinungen der Parteien zu den Aussagen
meinungen = {
    "Grüne": ["Ja, wir unterstützen das!", "Ja, wichtig für den Klimaschutz!", "Ja, Familien müssen unterstützt werden!", "Ja, Digitalisierung ist entscheidend!", "Ja, kostenloser Nahverkehr hilft allen!", "Nein, mehr Tierschutz ist nötig!", "Nein, erneuerbare Energien müssen gefördert werden!", "Ja, Grundeinkommen schafft soziale Sicherheit!", "Nein, Mietpreise müssen reguliert werden!", "Ja, Asylrecht muss gewahrt bleiben!"],
    "Linke": ["Ja, alle sollen gleiche Chancen haben!", "Ja, Klimaschutz geht vor!", "Ja, Reiche sollen mehr zahlen!", "Ja, Bildung muss kostenlos sein!", "Ja, Mobilität ist ein Grundrecht!", "Nein, Tierschutz ist eine Priorität!", "Nein, erneuerbare Energien brauchen Förderung!", "Ja, ein Grundeinkommen hilft gegen Armut!", "Nein, Mietpreise müssen begrenzt werden!", "Ja, keine Abschiebungen mehr!"],
    "SPD": ["Ja, aber mit Kompromissen!", "Ja, aber nicht zu schnell!", "Ja, aber wir müssen es finanzieren!", "Ja, aber Schulen müssen mitmachen!", "Ja, aber nur für Bedürftige!", "Nein, aber mit Unterstützung für Bauern!", "Nein, aber mit Augenmaß!", "Ja, aber mit Bedingungen!", "Nein, Mieten müssen begrenzt werden!", "Ja, aber kontrollierte Migration!"],
    "CDU": ["Nein, wir brauchen unterschiedliche Schulen!", "Nein, zu teuer für Autofahrer!", "Nein, Familien sollen selbst vorsorgen!", "Ja, aber nicht als Pflicht!", "Nein, das kostet zu viel!", "Ja, Bauern sollten selbst entscheiden!", "Ja, keine staatliche Förderung für erneuerbare Energien!", "Nein, Leistung muss sich lohnen!", "Ja, freie Mietpreise!", "Nein, Migration muss begrenzt werden!"],
    "AfD": ["Nein, das alte System funktioniert!", "Nein, Klimawandel ist nicht menschengemacht!", "Nein, weniger Staat, mehr Eigenverantwortung!", "Nein, Digitalisierung ist überbewertet!", "Nein, keine staatlichen Zuschüsse für Verkehr!", "Ja, Tierschutz ist überreguliert!", "Ja, erneuerbare Energien sollen sich selbst finanzieren!", "Nein, kein Geld ohne Arbeit!", "Ja, Markt regelt Mieten!", "Nein, keine Aufnahme von Migranten!"],
    "FDP": ["Nein, Leistung muss sich lohnen!", "Nein, Technologie soll es lösen!", "Nein, keine zusätzlichen Ausgaben!", "Ja, aber mit privaten Anbietern!", "Nein, keine Gratisleistungen!", "Ja, Tierschutz über den Markt regeln!", "Ja, erneuerbare Energien ohne Subventionen!", "Nein, staatliche Hilfe nur für Bedürftige!", "Ja, Mietpreise sollen frei bleiben!", "Nein, nur qualifizierte Migration!"]
}

# Positionen der Parteien (1 = vollständige Übereinstimmung, 0.75 = eher Zustimmung, 0.5 = neutral, 0.25 = eher Ablehnung, 0 = keine Übereinstimmung)
positionen = np.array([
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1],  # Grüne
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1],  # Linke
    [1, 1, 1, 1, 1, 0, 0, 0.75, 0, 1],  # SPD
    [0, 0, 0, 0.75, 0, 1, 1, 0, 1, 0],  # CDU
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],  # AfD
    [0, 0, 0, 0.75, 0, 1, 1, 0, 1, 0]  # FDP
])
