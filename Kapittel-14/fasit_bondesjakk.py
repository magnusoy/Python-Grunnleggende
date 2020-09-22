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
player, computer = "", ""
# Corners, Center and Others, respectively
moves = ((1,7,3,9), (5,), (2,4,6,8))
# Winner combinations
winners = ((0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8), 
           (0,4,8), (2,4,6))

# Table
tab = range(1,10)

def print_board():
    x = 1
    for i in board:
        end = " | "
        if x % 3 == 0:
            end = " \n"
            if i != 1: end+="---------\n";
        char = " "
        if i in ("X", "O"): char = i;
        x += 1
        print(char, end=end)

def select_char():
    chars=("X", "O")
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)


def computer_move():
    move =- 1
    # If I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break

    if move == -1:
       # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move = i
                break

    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
    return make_move(board, computer, move)


def space_exist():
    return board.count("X") + board.count("O") != 9


player, computer = select_char()
print(f"Spiller er [{player}] og datamaskin er [{computer}]")
result = "Uavgjort!"

while space_exist():
    print_board()
    move = int(input("Ditt trekk: [1-9] : \n"))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Ulovlig trekk, Prøv igjen!")
        continue
    if won:
        result = "Gratulerer, du vant!"
        break
    elif computer_move()[1]:
        result = "Du tapte!"
        break

print_board()
print(result)