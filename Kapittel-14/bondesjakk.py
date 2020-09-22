"""
Bondesjakk

Bondesjakk er et brettspill der målet er å få tre av sine symboler på en rett linje.
Spillet er laget for 2 spillere hvor hver spiller har sitt symbol som regel representert av en X eller en O. 
Spilleflaten er et kvadrat med tre ganger tre ruter. 
Spillerne har kun lov til å sette symbolet sitt i en tom rute om gangen før de skifter tur. 
Førstemann som har tre av sine symboler langs en rett linje, har vunnet spillet.

Den andre spilleren i dette tilfellet blir datamaskinen.
Du får tildelt en funksjon som setter opp rutene for banen.
I tillegg er vinnerkombinasjonene skrevet ned.

* Spillet kan bli laget på mange måter, så om du ikke ønsker
å bruke tildelt hjelpemiddel så tregner du ikke det.

* Logikken til datamskinen kan du lage til å være tilfeldig om
du syns det blir for vanskelig å planlegge beste trekk.

"""

import random


board = [slot for slot in range(0,9)]
player, computer = '', ''
# Corners, Center and Others, respectively
moves = ((1,7,3,9), (5,), (2,4,6,8))
# Winner combinations
winners = ((0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8), 
           (0,4,8), (2,4,6))

def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X', 'O'): char = i;
        x += 1
        print(char, end=end)

print_board()