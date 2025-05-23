# -*- coding: utf-8 -*-
"""Centskat_App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wL99GRCexKDP58rqnGmGmsBeBX3yKvBY
"""

code = '''import streamlit as st

st.title("Skatabrechnung – Durchschnittsvariante")

# Eingabe der Punktzahlen
st.markdown("### Punktestände eingeben:")
namen = []
punkte = {}

anzahl_spieler = st.number_input("Anzahl der Spieler*innen", min_value=3, max_value=6, value=3)

for i in range(anzahl_spieler):
    name = st.text_input(f"Name Spieler*in {i+1}", key=f"name_{i}")
    punkt = st.number_input(f"Punkte für {name}", key=f"punkte_{i}", step=1)
    if name:
        namen.append(name)
        punkte[name] = punkt

if len(punkte) == anzahl_spieler:
    durchschnitt = sum(punkte.values()) / len(punkte)
    differenzen = {n: round(p - durchschnitt, 2) for n, p in punkte.items()}
    zahler = {n: -d for n, d in differenzen.items() if d < 0}
    empfaenger = {n: d for n, d in differenzen.items() if d > 0}
    gesamtschuld = sum(zahler.values())

    transfers = []
    for z_name, z_betrag in zahler.items():
        for e_name, e_betrag in empfaenger.items():
            betrag = round((z_betrag / gesamtschuld) * e_betrag, 2)
            if betrag > 0:
                transfers.append((z_name, e_name, round(betrag / 100, 2)))  # in Euro

    st.markdown("### Ausgleichszahlungen:")
    for von, an, betrag in transfers:
        st.write(f"{von} zahlt **{betrag:.2f} €** an {an}")
'''

# Datei speichern
with open("skat_app.py", "w") as f:
    f.write(code)