"""
Oppgave 1

Importer random og bruk
randint() til å generere et tilfeldig tall mellom 1 - 100
"""
import random
print(random.randint(1, 100))

"""
Oppgave 2

Fra random skal du importere choise
Deretter bruk funksjonen til å 
tilfeldig velge en verdi fra en liste.
"""
lst = ["A", "B", "C", "D", "E", "F"]
print(random.choice(lst))

"""
Oppgave 3

https://docs.python.org/3/library/turtle.html

Åpne linken og finn ut hvordan du skal bruke
modulen til å tegne:

1) Trekant
2) Firkant
"""
import turtle
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

"""
Oppgave 4

Lag din egen modul som inneholder
en funksjon som finner antall vokaler i
en tekst.

Eks:
find_vowels("Hei alle sammen, her er det mange vokaler") -> 14
"""

# from modul import find_vowels
# Lag en fil kalt: modul.py og legg inn funksjonen
# def find_vowels(txt):
#     total = 0
#     vowels = ('a', 'e', 'i', 'o', 'u', 'æ', 'ø', 'å')
#     for char in txt:
#         if char in vowels:
#             total += 1
#     return total



print(find_vowels("Hei alle sammen, her er det mange vokaler"))