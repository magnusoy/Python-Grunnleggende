# Løfte egen feil
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero") 

# Try, Except
def divide(x, y): 
    try:
        result = x // y 
    except ZeroDivisionError: 
        print("Det er ikke mulig å dividere med 0") 

# Try, Except, Finally
valid_number = False
while not valid_number:
    try:
        number = int(input("Ditt tall: "))
        valid_number = True
    except ValueError:
        print("[ERROR] Brukerinput er ikke et tall...")
    finally:
        if not valid_number:
            print("Prøv igjen...")
        else:
            print(number)