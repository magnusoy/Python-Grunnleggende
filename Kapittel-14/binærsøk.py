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
    # Skriv din kode her



numbers = random.sample(range(1, 50), 45)
print(numbers)
print(binary_search(numbers, 12))