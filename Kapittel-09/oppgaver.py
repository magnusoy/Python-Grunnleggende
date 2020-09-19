"""
Oppgave 1

Lag en funksjon make_noise som printer "ALLE MÅ ROPE"
Deretter bruk funksjonen
"""

"""
Oppgave 2
Lag en funksjon speak_cow som returnerer "MOOOO"
Print så ut resultatet fra funksjonen
"""


"""
Oppgave 3
Lag en funksjon som generer 50 partall.
Den skal returnere en liste med alle partallene.
"""

"""
Oppgave 4

Lag funksjonen yell som tar inn en string argument.
Den returnerer argumentet i STOREBOKSTAVER!

Eks: yell("gå vekk") -> GÅ VEKK!
"""


"""
Oppgave 5

Fiks funksjonen!

Funksjonen count_dollar_signs fungerer ikke som den skal.
Den tar i mot en tekst og skal returne antall ganger $ er skrevet.

Eks. count_dollar_signs($uper mye $ukker) -> 2

Problemet er at for en eller annen grunn så returnerer den bare 0 eller 1...
"""

def count_dollar_signs(txt):
    count = 0
    for char in txt:
        if char == '$':
            count += 1
        return count

print(count_dollar_signs("$uper mye $ukker"))



"""
Oppgave 6

Skriv en funksjon speak som tar inn et dyr som parameter.

Hvis dyret er "gris", returner "nøff"
Hvis dyret er "and", returner "kvakk"
Hvis dyret er "katt", returner "meow"
Hvis dyret er "hund", returner "voff"
Hvis dyret er noe annet, returner ?
Hvis dyret IKKE er nevn så skal den returnere
det hunden sier.

Eks.

speak() -> "voff"
speak("gris") -> "nøff"
speak("and") -> "kvakk"
speak("katt") -> "meow"
speak("hund") -> "voff"
speak("giraff") -> "?"
"""


""" 
Oppgave 7

Lag en funksjon intersection som aksepterer to lister.
Sjekk hvilke verdier i listene som er like
Returner en liste som inneholder de like verdiene.

Eks.
intersection([1, 2, 3], [2, 3, 4]) -> [2, 3]
intersection(["a", "b", "z"], ["x", "y", "z"]) -> ["z"]
"""

def intersection():
    pass