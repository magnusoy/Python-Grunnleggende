"""
Oppgave 1

Løft din egen exception med egendefinert melding.

Kommenter ut kodebiten etter at du har testet den.
"""



"""
Oppgave 2

Gitt følgende funksjon task_2
Fiks funksjonen til å ikke kræsje om brukeren
legger inn bokstaver.
Ta også høyde for nulldivisjon.

Tips: except kan skrives flere ganger!
"""
def task_2(num1, num2):
    return num1 / num2

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