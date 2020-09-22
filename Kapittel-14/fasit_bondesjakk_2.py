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
player, computer = 'X', 'O'
someone_won = False
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
            if i != 1: 
                end += '---------\n';
        char=' '
        if i in ('X', 'O'): 
            char = i;
        x += 1
        print(char, end=end)

def can_win(brd, player):
    for winning_slots in winners:
        win = True
        for slot in winning_slots:
            if brd[slot] != player:
                win = False
                break
        if win:
            break
    return win

print_board()

moves = [slot for slot in range(1, 10)]

while len(moves) != 0 and not someone_won:

    user_move = int(input("Hvor vil du krysse av?\n"))
    board[user_move-1] = player
    moves.remove(user_move)
    print_board()
    if can_win(board, player):
        print("Du vant!")
        someone_won = True
        break
    computer_move = random.choice(moves)
    print(computer_move)
    moves.remove(computer_move)
    board[computer_move-1] = computer
    print_board()
    if can_win(board, computer):
        print("Du tapte!")
        someone_won = True
        break
    if len(moves) == 0 and not someone_won:
        print("Uavgjort!")