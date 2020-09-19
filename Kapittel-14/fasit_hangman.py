import random

print("\n\nVelkommen til Hangman!\n\n")

word = random.choice(["Hus", "Politi", "By", "Stein", "Regn", "Maskin", "Lokomotiv"])
guesses = ''
turns = 10

while turns > 0:         
    failed = 0              
    for char in word:      
        if char in guesses:    
            print(char)    
        else:
            print("_")     
            failed += 1    
    if failed == 0:        
        print("\nDu vant!\n")  
        break              

    guess = input("Gjett bokstav:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nFeil")    
        print(f"\nDu har {turns} forsøk igjen\n") 
 
        if turns == 0:           
            print("\nDu tapte!\n")  