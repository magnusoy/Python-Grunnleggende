"""
Oppgave 1

Løft din egen exception med egendefinert melding.
"""



"""
Oppgave 2

Gitt følgende funksjon task_2
Fiks funksjonen til å ikke kræsje om brukeren
legger inn bokstaver.
Ta også høyde for nulldivisjon.

Tips: except kan skrives flere ganger!
"""

"""
Oppgave 3

Du skal lage et felt hvor brukere kan skrive inn passordet sitt.

FormulaError er en egendefinert exception.
Løft denne exceptionen om input fra brukeren ikke
tilfredsstiller følgende krav:
1) Passord minst 8 tegn
2) Skal inneholde bokstaver og tall
3) Skal inneholde minst 1 tegnene: (.  !  &  ?)
"""

class InvalidPasswordError(Exception): pass