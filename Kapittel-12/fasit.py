"""
Oppgave 1

Løft din egen exception med egendefinert melding.

Kommenter ut kodebiten etter at du har testet den.
"""

# a = 2
# if a < 3:
#     raise ValueError("Verdien er for lav")


"""
Oppgave 2

Gitt følgende funksjon task_2
Fiks funksjonen til å ikke kræsje om brukeren
legger inn bokstaver.
Ta også høyde for nulldivisjon.

Tips: except kan skrives flere ganger!
"""
def task_2(num1, num2):
    result = 0
    try:
        result =  num1 / num2
    except ZeroDivisionError:
        print("Kan ikke dele med 0")
    except TypeError:
        print("Kan ikke dele med bokstaver")
    finally:
        return result

print(task_2(2, 4))
print(task_2(2, 0))
print(task_2('s', 'a'))

"""
Oppgave 3

Du skal lage et felt hvor brukere kan skrive inn passordet sitt.

InvalidPasswordError er en egendefinert exception.
Løft denne exceptionen om input fra brukeren ikke
tilfredsstiller følgende krav:
1) Passord minst 8 tegn
2) Skal inneholde minst 1 tegnene: (.  !  &  ?)

Tips: Bruk any for punkt 2
"""

class InvalidPasswordError(Exception): pass

password = input("Ditt passord: ")
if len(password) > 8 and any(char in ['.', '!', '&', '?'] for char in password):
    print("Sterkt passord!")
else:
    raise InvalidPasswordError("Svakt passord!")