"""
Oppgave 1

Definer en liste: my_stuff
Den skal være 4 elementer lang
Den kan inneholde hva som helst, men det
skal værtfall være 1 string og 1 float.
"""
my_stuff =["Hei", 12.3, 4, True]

"""
Oppgave 2

Definer en liste: numbers
Den skal inneholder all nummer mellom 1 og 100

(Ikke skriv inn dette manuelt)
"""
numbers = []
for number in range(2, 100):
    numbers.append(number)

"""
Oppgave 3

Vi har invitert en gjeng hjem til fest.
Desverre så har jeg klart å skrive navnene feil...
Hjelp meg å rette opp i feilene

1) Hanna -> Hannah
2) Haron -> Harun
3) caroline -> Karoline
"""

people = ["Hanna", "Leif", "Karsten", "Haron", "Janne", "caroline"]
people[0] = "Hannah"
people[3] = "Harun"
people[-1] = "Karoline"
print(people)

"""
Oppgave 4

Jeg har en liste med forskjellige lyder.
Jeg ønsker å loope over og legge sammen alle til en string.
I tillegg ønsker jeg at alle bokstavene i stringen skal være STOREBOKSTAVER
Lagre resultatet i result og print det ut til terminalen
"""

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
full_sound = ""
for sound in sounds:
    full_sound += sound
print(full_sound)

"""
Oppgave 5

Lag en tom liste.
Legg til verdiene følgende verdier:
1) "Magnus"
2) "Nils"
3) "Sofie"

"""

lst = []
lst.extend(["Magnus", "Nils", "Sofie"])
print(lst)

"""
Oppgave 6

Lag en tom liste.
Legg til verdiene følgende verdier:
1) "Magnus"
2) "Nils"
3) "Sofie"

* Fjern det siste elementet i listen
* Fjern det første elementet i listen
* Legg til stringen "Ferdig" i starten av listen
"""

lst = []
lst.extend(["Magnus", "Nils", "Sofie"])
lst.pop()
lst.pop(0)
lst.insert(0, "Ferdig")
print(lst)