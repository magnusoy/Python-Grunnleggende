"""
Oppgave 1

Lag en variabel som inneholder
følgende tekst: Dette er første delen
"""

part1 = "Dette er første delen"

"""
Oppgave 2

Lag en annen variabel som inneholder
følgende tekst: og dette er den andre delen av teksten.

Bruk variabelen du laget i Oppgave 1 sammen med variabelen
fra denne Oppgaven til å lage en ny variabel som inneholder
følgende tekst: Dette er første delen, og dette er den andre delen av teksten.

Avslutt med å printe resultatet i terminalen.
"""

part2 = " og dette er den andre delen av teksten."
concat = part1 + ',' + part2
print(concat)

print("#"*20) # Ignorer
"""
Oppgave 3

Lag en variabel som inneholder tekst som deler teksten ved bruk av en avbruddsekvens

Avslutt med å printe resultatet i terminalen.
"""

escape_string = "Heisann,\nHvordan går det?"
print(escape_string)

print("#"*20) # Ignorer
"""
Oppgave 4

Det er allerede laget to variabel som inneholder by og land.
Print ut følgende tekst til terminalen: Jeg kommer fra Oslo, Norge.

(Du står fritt fram for å bruke hvilken som helst formateringsmetode)
"""

city = "Oslo"
country = "Norge"
print(f"Jeg kommer fra {city}, {country}")

print("#"*20) # Ignorer
"""
Oppgave 5

Det er lagt en variabel med følgende tekst: Det skyfritt på himmelen, 24 grader i skyggen og solen går ned 23:45.
Hent ut følgende verdier og lagre dem i variabler:
1 ) skyfritt
2 ) 24
3 ) 23:45

Deretter printer du dem ut i terminalen med et linjeskift mellom hver verdi.
"""

txt = "Det skyfritt på himmelen, 24 grader i skyggen og solen går ned 23:45."
sky = txt[4:12]
temperature = txt[26:28]
sunset = txt[-6:-1]
print(f"{sky}\n{temperature}\n{sunset}")

print("#"*20) # Ignorer
