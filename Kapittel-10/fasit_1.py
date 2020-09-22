"""
Oppgave 1

lag en funksjon contains_pink som aksepterer hvilket som helst antall nummer argumenter.
Den skal returnere True om "pink" finnes i argumentene.
Om ikke skal den returnere False

Eks.
contains_pink(21, "pink") -> True
contains_pink("green", False, 37, "blue", "hello world") -> False
contains_pink("pink") -> True
contains_pink("PiNK") -> False
contains_pink(1, 2, 3) -> False
"""
def contains_pink(*colors):
    return "pink" in colors

print(contains_pink(21, "pink"))
print(contains_pink("green", False, 37, "blue", "hello world") )
print(contains_pink("pink"))
print(contains_pink("PiNK"))
print(contains_pink(1, 2, 3))

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
def combine_words(word, **kwargs):
    if "suffix" in kwargs:
        return word + kwargs["suffix"]
    elif "prefix" in kwargs:
        return kwargs["prefix"] + word
    return word

print(combine_words("Fantastisk"))
print(combine_words("Fantastisk", prefix="Fremmerst"))
print(combine_words("Fantastisk", suffix="bakerst"))
print(combine_words("Arbeid", suffix="er"))
print(combine_words("mann", prefix="Salgs"))


