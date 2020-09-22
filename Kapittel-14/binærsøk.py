"""
Binærsøk

Navnet er tydelig nok til å gi en oversikt over oppgaven. 
Programmet krever at du lager en liste med tall mellom 0 til hvilket område du foretrekker, 
med hvert påfølgende nummer som har en forskjell på 2 mellom dem.

Når brukeren skriver inn et tilfeldig tall som skal søkes, 
begynner programmet søket ved å dele listen i to halvdeler. 
Første halvdel blir søkt etter ønsket antall, og hvis den blir funnet, 
blir den andre halvparten avvist og omvendt. 
Søket fortsetter til tallet blir funnet eller størrelsen på undergruppen blir null. 
"""

import random

def binary_search(lst, number):
    """
    docstring
    """

    mid = 0
    start = 0
    end = len(lst)
    step = 0

    while (start <= end):
        step +=  1
        mid = (start + end) // 2

        if number == lst[mid]:
            return mid

        if number < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


numbers = random.sample(range(1, 50), 46)
numbers.sort()
print(numbers)
print(binary_search(numbers, 12))