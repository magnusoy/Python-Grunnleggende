"""
Oppgave 1
Spør i terminalen hvor brukeren kommer fra.

Print brukerinputen til terminalen.
"""
#city = input("Hvor kommer du ifra? ")
#print(f"Brukeren kommer fra {city}")

print("\n"*3)  # Ignorer
"""
Oppgave 2

Sjekk om x og y er like store.

"""

x = 0.1
y = -0.1

if x == y:
    print("De er like store!")


print("\n"*3)  # Ignorer
"""
Oppgave 3

Sjekk om a er mindre enn b.

"""
a = 234
b = 443

if a < b:
    print("a er mindre enn b")


print("\n"*3)  # Ignorer
"""
Oppgave 4

Få brukerinput, hvor du spør om navnet.
Sjekk om navnet er lenger enn 6 bokstaver.
Om det er kortere. Hvor mange bokstaver mangler
navnet?

Print resultetene i terminalen.
"""
"""
name = input("Ditt navn: ")
if len(name) > 6:
    print("Navnet er lengre enn 6 bokstaver!")
else:
    rest = 7 - len(name)
    print(f"{name} mangler {rest} bokstaver!")
"""

print("\n"*3)  # Ignorer
"""
Oppgave 5 (Utfordring)

Det blir generert et tilfeldig tall.

Spør i terminalen hva brukeren tror verdien er.

Sjekk om verdien stemmer.
Print om brukeren gjetter ritkig tall.

Om brukeren bommer med bare 1, så skal
du printe at brukeren bommet med 1.

Om brukeren bommer med mer enn 1,
så bare print det riktige tallet.

"""

import random # Ignorer
random_number = random.randint(1, 10) # Generer et tilfeldig tall fra 1 opp til og med 10

user_guess = int(input("Det tilfeldige tallet er: "))

if user_guess == random_number:
    print("Riktig!")
elif user_guess-1 == random_number:
    print("Nesten! Du bommet bare med 1!")
elif user_guess+1 == random_number:
    print("Nesten! Du bommet bare med 1!")
else:
    print(f"Ikke i nærheten!\nDet tilfeldige tallet var: {random_number}!")

