# Lage en tom liste
lst = []

# Lage en liste med verider
lst = [1, 2, 3, 4, 5, 6]

# Hente ut det første elementet i en liste
element = lst[0]

# Hente ut det siste elementet i en liste
element = lst[-1]

# Lage en ny liste ut fra en del av en større liste
sub_lst = lst[0:3]

# Lage en ny liste ut fra en del av en større liste
sub_lst = lst[-4:-1]

# Lagre verdien fra element 0 i en variabel
num = lst[0]

# Endre verdien til elementet i listen
lst[3] = 9

# Endre verdiene til elementene i listen
lst[0:2] = [8, 0]

# Fjern det siste elementet
lst.pop()

# Fjern det første elementet
lst.pop(0)

# Legg til 6 i slutten av listen
lst.append(6)

# Legg til 1 i starten av listen
lst.insert(0, 1)

# Sorter listen i stigende rekkefølge
lst.sort()

# Reverser listen til synkende rekkefølge
lst.reverse()

# Legg til en liste i listen
lst.extend([10, 11, 12, 13, 14, 15])

# Iterer gjennom listen
for index in range(len(lst)):
    element = lst[index]
    print(element)

# Iterer gjennom listen
for element in lst:
    print(element)

# Sjekk om listen inneholder verdien 1
if 1 in lst:
    print("True")

# Generer en stor liste fra 0 - 1000
big_lst = list(range(1001))
print(big_lst)

# Generer en stor liste fra 0 - 1000
big_lst = [x for x in range(1001)]
print(big_lst)

# Generer en liste fra 0 - 100 med partall
even_numbers = []
even_numbers.append(list(range(0, 101, 2)))
print(even_numbers)

# Generer en liste fra 0 - 100 med partall
even_numbers = [x for x in range(0, 100) if x % 2 == 0]
print(even_numbers)