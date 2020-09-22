"""
Hangman

Ordet man skal forsøke å gjette seg frem til, 
angis med en rad med streker, der hver strek angir én bokstav.
Hvis spilleren som gjetter foreslår en bokstav som finnes i ordet, 
skriver den andre spilleren denne bokstaven i alle de riktige posisjonene.

Vær kreativ å lag din egen løsning basert på din fatning av spillet!

* Du får tildelt et tilfeldig ord som blir brukt i spillet.
"""


import random

print("\n\nVelkommen til Hangman!\n\n")

word = random.choice(["Hus", "Politi", "By", "Stein", "Regn", "Maskin", "Lokomotiv"])
# Skriv din kode under her

