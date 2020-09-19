"""
Oppgave 1

lag en funksjon contains_pink som aksepterer hvilket som helst antall nummer argumenter.
Den skal returnere True om "pink" finnes i argumentene.
Om ikke skal den returnere False

Eks.
contains_pink(21, "pink") -> True
contains_pink("green", False, 37, "blue", "hello world") -> False
contains_pink("pink") -> True
contains_pink("PiNK") -> True
contains_pink(1, 2, 3) -> False
"""


""" 
Oppgave 2

Skriv en funksjon combine_words som aksepterer en enkel string.
Hvis en prefix er inkludert skal denne legges til i starten av ordet.
Hvis en suffix er inkludert skal denne legges til i slutten av ordet.
Hvis ingen av delene er inkludert så returneres ordet.

Eks.
combine_words("Fantastisk") -> "Fantastisk"
combine_words("Fantastisk", prefix="Fremmerst") -> "FremmerstFantastisk"
combine_words("Fantastisk", suffix="bakerst") -> "Fantastiskbakerst"

combine_words("Arbeid", suffix="er") -> "Arbeider"
combine_words("mann", prefix="Salgs") -> "Salgsmann"
"""

"""
Oppgave 3

Jeg har laget funksjonen count_sevens for deg.

Du skal først bruke den med argumentene 1, 4, 7 og lagre resultatet i result1
Deretter bruker du funksjonen igjen med å legge inn numbers.
Lagre dette resultatet i variabel result2

"""

def count_sevens(*args):
    return args.count(7)

numbers = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,
        68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,
        56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,
        9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,
        12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,
        6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,
        8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]



"""
Oppgave 4

Du skal lage en funksjon calculate som aksepterer en liste av nøkkelord argument:

make_float, en boolean som returnerer en float hvis True, eller en int hvis False
operation, som er enten "add", "subtract", "multiply" eller "divide"
first, som er et tall
second, som er et annet tall

Funksjonen skal returnerer resultatet av å kjøre akkurat det du legger inn.
Altså gjøre den nevnte operasjonen med det første og andre tallet.
Husk at make_float bestemmer om det returneres en float eller int.

Eks.
calculate(make_float=False, operation='add', first=2, second=4) -> 6
calculate(make_float=True, operation='divide', first=3.5, second=5) -> 0.7
"""

def calculate():
    pass

