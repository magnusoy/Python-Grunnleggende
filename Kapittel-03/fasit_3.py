"""
Oppgave 1

Gjør om all teksten i variabelen til store bokstaver.
"""

txt = "vI LæReR om PYTon i dETte kurSEt"
txt2 = txt.upper()
print(txt2)

"""
Oppgave 2

Slutter teksten med: pappesker?
"""

txt = "Her var det veldig mange tomme pappesker"
result = txt.endswith("pappesker")
print(result)

"""
Oppgave 3

Finn ut om teksten inneholder ordet "is" og print ut indeksen.
"""

txt = "På tivoli er det mange som spiser is, og tar karuseller."
result = txt.find("is")
print(result)

"""
Oppgave 4

Bytt ut alle komma med mellomrom.
"""

txt = "Hund,Katt,Geit,Bjørn,Gaupe,Ørn,Spurv"
result = txt.replace(",", " ")
print(result)