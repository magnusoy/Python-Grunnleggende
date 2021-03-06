"""
Oppgave 1

Print alle tallene fra 1 til 100
"""
for number in range(101):
    print(number)


"""
Oppgave 2

Legg sammen alle tallene fra 1 til 100
"""
total = 0
for number in range(101):
    total += number
print(total)


"""
Oppgave 3

Legg sammen alle oddetallene fra 10 til 20
Lagre resultatet i "result"
"""

result = 0
for number in range(10, 21):
    if number % 2 != 0:
        result += number
print(result)

"""
Oppgave 4

Få brukerinput som er antall ganger
følgende skal printes ut i terminalen: "Gå å vask rommet!"
"""
times = int(input("Antall ganger: "))
for _ in range(times):
    print("Gå å vask rommet!")

"""
Oppgave 5

Loop gjennom tallene 1 til 20
1) For 4 og 13; print "x er uheldig"
2) For partall; print "x er partall"
3) For oddetall; print "x er oddetall"

(x symboliserer tallet i oppgaveksten)
Eks. 5 er uheldig
Eks. 2 er partall
Eks. 15 er oddetall
"""
for number in range(1, 20):
    if number == 4 or number == 13:
        print(f"{number} er uheldig")

    if number % 2 == 0:
        print(f"{number} er partall")
    else:
        print(f"{number} er oddetall")



"""
Oppgave 6

Lag en loop som printer følgende:
*
**
***
****
*****
******
*******
********
*********
"""

sequence = ""
for step in range(9):
    sequence += "*"
    print(sequence)


"""
Oppgave 8 (Utfordring)

Gjett datamaskinens nummer!

Datamaskinen gjetter et tall mellom 1 - 10
Be brukeren prøve å gjette tallet.
Om brukeren ikke gjetter ritkig så skal han bli spurt igjen
Dette skjer helt til brukeren gjetter riktig.
Om brukeren treffer ritkig tall så avslutter koden.

Om brukeren skriver for stort tall så skal du be brukeren prøve et lavere tall.
Om brukeren skriver for lite tall så skal du be brukeren prøve et høyere tall.
"""

from random import randint

random_number = randint(1, 10)

correct_answer = False

while not correct_answer:
    user_guess = int(input("\nHva tror du nummeret er?\n"))
    if user_guess == random_number:
        print("Wohu! Riktig!")
        correct_answer = True
    elif user_guess > random_number:
        print("Feil! Tallet er for høyt!")
    else:
        print("Feil! Tallet er for lavt!")
