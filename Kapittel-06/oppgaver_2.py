"""
Oppgave 1

Gitt listen ["Magnus", "Frank", "Kristina"],
lag en variabel kalt first_letters som er en
ny liste som inneholder den første bokstaven i hvert navn.
"""

names = ["Magnus", "Frank", "Kristina"]


"""
Oppgave 2

Gitt listen [1, 2, 3, 4, 5, 6],
lag en variabel kalt even_numbers som er en
ny liste som inneholder bare partall.
"""

numbers = [1, 2, 3, 4, 5, 6]


"""
Oppgave 3

Du har en liste med ord: ["Bil", "Alarm", "Sofa", "Stein", "Glass"]
Lag en variabel kalt words_reversed som inneholder hvert ord reversert.
"""

words = ["Bil", "Alarm", "Sofa", "Stein", "Glass"]



"""
Oppgave 4
Du har en liste: [[7, 1, 2], [4, 5, 0], [6, 1, 9]]
Dekomponer listen til for eks. [7, 1, 2] å legg sammen summen av verdiene.
Legg summen av alle 3 nestede listene i en liste.
Resultatet til slutt skal bli: [10, 9, 16]

Tips: Dette er en nested liste. Prøv en for loop i en for loop.
"""

"""
Oppgave 5

Ved bruk av loops, så skal du lage følgende liste:
[
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

Altså en 10x10 liste.
Ikke bry deg om formateringen av listen. Den er presentert på denne
måten for at det skal være oversiktlig.

Ditt resultat blir noe likt dette:
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

For å bekrefte om du har gjort ritkig:
print(f"{len(result)}x{len(result[0])}") -> 10 x 10
"""

result = []
for i in range(0, 10):
    result.append(list(range(10)))

print(result)
print(f"{len(result)}x{len(result[0])}")