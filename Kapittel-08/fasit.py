"""
Oppgave 1
Lag en variabel numbers som er en tuple of inneholder 1, 2, 3 og 4
"""
numbers = (1, 2, 3, 4)
print(numbers)

""" 
Oppgave 2
Lag en variabel number som inneholder verdien 1, som er hentet ut fra 
din tuple numbers.
"""
number = numbers[0]
print(number)

"""
Oppgave 3
Lag en variabel kalt static_values som er resultatet av listen konvertert til en tuple.
"""

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
static_values = tuple(values)
print(static_values)

"""
Oppgave 4

Lag en variabel kalt unique_numbers som er et set som inneholder bare unike verdier fra listen
"""

numbers = [1, 3, 1, 5, 2, 5, 1, 2, 5]
unique_numbers = set(numbers)
print(unique_numbers)