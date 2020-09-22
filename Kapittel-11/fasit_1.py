"""
Oppgave 1

Skriv en lambda som aksepterer et tall og høyer det opp i 3
lambda kan hete cube
"""
cube = lambda x: x**3
print(cube(10))


"""
Oppgave 2

Lag en funksjon decrement_list som tar inn en liste med tall som parameter.
Den skal returnere en kopi av listen hvor alle verdiene er i dekrementert med 1.

Eks:
decrement_list([1, 2, 3]) -> [0, 1, 2]
decrement_list([20, 14, 11]) -> [19, 13, 10]

Tips: Bruk map()
"""
def decrement_list(lst):
    return list(map(lambda n: n-1, lst))

print(decrement_list([1, 2, 3]))
print(decrement_list([20, 14, 11]))
"""

Oppgave 3

Lag en funksjon remove_negatives som tar inn en liste med tall og returnerer en kopi av listen
hvor alle de negative tallene er fjernet.

Eks:
remove_negatives([-1, 3, 4, -99]) -> [3, 4]
remove_negatives([-2, 0, 1, 2, 3, 5, 11, -1]) -> [0, 1, 2, 3, 5, 11]
remove_negatives([50, 60, 80]) -> [50, 60, 80]

Tips: Bruk filter()
"""
def remove_negatives(numbers):
    return list(filter(lambda number: number >= 0, numbers))

print(remove_negatives([-1, 3, 4, -99]))
print(remove_negatives([-2, 0, 1, 2, 3, 5, 11, -1]))
print(remove_negatives([50, 60, 80]) )

"""
Oppgave 4

Lag en funksjon is_all_strings som tar inn en iterable og 
returnerer True hvis den iterablen inneholder
bare strings. Om ikke skal den returere False

Eks:
is_all_strings(["a", "b", "c"]) -> True
is_all_strings([1, "a", "b", "c"]) -> False
is_all_strings(["heisann", "farvell"]) -> True

Tips: Bruk all()
"""

def is_all_strings(lst):
    return all([type(elem) == str for elem in lst])

print(is_all_strings(["a", "b", "c"]))
print(is_all_strings([1, "a", "b", "c"]) )
print(is_all_strings(["heisann", "farvell"]))

"""
Oppgave 5

lag en funksjon extremes som tar inn en iterable. 
Den skal returere en tuple som inneholder
den laveste og høyeste verdien fra elementene.

Eks:
extremes([1, 2, 3, 4, 5, 6]) -> (1, 6)
extremes([75, 234, 54, 76, 1, -4]) -> (-4, 234)
extremes("norge") -> ("e", "r")

Tips: Bruk min() og max()
"""

def extremes(numbers):
    return(min(numbers), max(numbers))

print(extremes([1, 2, 3, 4, 5, 6]))
print(extremes([75, 234, 54, 76, 1, -4]) )
print(extremes("norge"))



"""
Oppgave 6

Lag en funksjon max_magnitude som tar inn en liste med tall.
Den skal returnere tallet som er lengt unna 0 (magnitude).

Eks:
max_magnitude([310, 33, -190]) -> 310
max_magnitude([464, -234, -1990]) -> 1990
max_magnitude([-310, -33, -190]) -> 310
"""

def max_magnitude(numbers):
    return max(abs(number) for number in numbers)

print(max_magnitude([310, 33, -190]))
print(max_magnitude([464, -234, -1990]))
print(max_magnitude([-310, -33, -190]))