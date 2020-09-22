"""
Du får tildelt en API som returnerer 10 spørsmål med svaralternativer
Du skal lage et spill ut av de spørsmålene.
Hvert spørsmål er tilfeldig og skal endres for hver runde.
Brukeren skal kunne velge mellom 1 - 4 for hva som er riktig alternativ.
Etter hvert spørsmål skal poengscoren dukke opp før neste spørsmål.

Du må legge til requests modulen før du kan starte.
pip install requests


Tips: Bli kjent med dataen førut. Bruk forskjellige dict og liste methoder
        for å bli kjent med dataen.
    
     Lag først en løsning som tar for seg bare 1 spørsmål.
        Utvid så programmet med en løkke for å ta alle spørsmålene
    
     Bruk shuffle for å rotere svaralternativene
"""

from random import shuffle

try:
    import requests  # Husk å importer modul
except ModuleNotFoundError:
    print("Last ned modulen. pip install requests")


URL_API = "https://opentdb.com/api.php?amount=10"
response = requests.get(URL_API)
content = dict(response.json())
print(content)
