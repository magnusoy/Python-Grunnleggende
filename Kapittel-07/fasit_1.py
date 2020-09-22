"""
Oppgave 1
lag en dictionary som inneholder 3 nøkler og verdier.
Nøklene og verdiene er opp til deg.

"""
my_dict = {"Navn": "Magnus", "Alder": 25, "By": "Trondheim"}
print(my_dict)

"""
Oppgave 2
Du får tildelt en dictionary {"First": "Kari", "Last": "Nordmann"}.
Lag en string variabel som inneholder hele navnet.

print(full_name) -> Kari Nordmann
"""

person = {"First": "Kari", "Last": "Nordmann"}
full_name = f"{person['First']} {person['Last']}"
print(full_name)

"""
Oppgave 3

Det har vært noen gjestfrie personer som har donert penger.
Jeg ønsker å finne ut summen av alle donasjonene.

Tips: Bruk donations.values() for å få verdiene
"""

donations = dict(Per=250.0, Lene=888.99, Finn=130.0, Linus=990.5, Elisa=1500.0, Lisa=500.25, Markus=100.0)
total = 0
for value in donations.values():
    total += value
print(total)

"""
Oppgave 4

Finn ut om Magnus er en av de som har donert.
"""

donations = dict(Per=250.0, Lene=888.99, Finn=130.0, Linus=990.5, Elisa=1500.0, Lisa=500.25, Markus=100.0)
print("Magnus" in donations)