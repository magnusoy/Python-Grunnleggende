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
