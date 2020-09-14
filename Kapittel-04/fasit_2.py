"""
Oppgave 1

Du får tildelt en tekst.
Finn ut om teksten inneholder dette ordet: brød


"""

txt = "Jeg må huske å kjøpe brød på butikken etterpå!"

if "brød" in txt:
    print("Teksten inneholder ordet brød!")
else:
    print("Teksten inneholder IKKE ordet brød!")


print("\n"*3)
"""
Oppgave 2

Du får tildelt en tekst.
Finn ut om teksten inneholder disse ordene: ost, brød


"""

txt = "Jeg må huske å kjøpe brød, syltetøy og ost på butikken etterpå!"
if "brød" in txt and "ost" in txt:
    print("Teksten inneholder ordene brød og ost!")
else:
    print("Teksten inneholder IKKE ordene brød og ost!")


print("\n"*3)
"""
Oppgave 3

Du får tildelt en tekst.
Finn ut om teksten inneholder en av ordene: ost, brød, syltetøy


"""

txt = "Jeg må huske å kjøpe brød, syltetøy og ost på butikken etterpå!"
if "brød" in txt or "syltetøy" in txt or "ost" in txt:
    print("Teksten inneholder værtfall en av matvarene!")
else:
    print("Teksten inneholder IKKE noen matvarer!")


print("\n"*3)
"""
Oppgave 4

Du får tildelt en tekst.
Finn ut om teksten inneholder dette ordet: brød
Hvis ordet finnes, så skal du deretter finne ut om ordet er nevnt
i starten av teksten, eller i slutten.

"""

txt = "Jeg må huske å kjøpe brød"

if "brød" in txt:
    length_of_txt = len(txt)
    word_position_in_txt = txt.find("brød")
    if (length_of_txt - word_position_in_txt) < (length_of_txt // 2):
        print("Ordet ligger i slutten av teksten!")
    else:
        print("Ordet ligger i starten av teksten!")
else:
    print("Teksten inneholder IKKE ordet!")


print("\n"*3)
"""
Oppgave 5

En bruker skriver inn et tall.
Finn ut om tallet er et partall eller oddetall.
Om tallet er et oddetall, så skal du sjekke om tallet inneholder 1 eller 7.
Eksempel: 1,7, 11, 177, 21, 31, 101, 567

"""

number = int(input("Ditt tall:"))

if (number % 2) == 0:
    print("Det er et partall!")
else:
    print("Det er et oddetall!")
    num_as_str = str(number)
    if "1" in num_as_str or "7" in num_as_str:
        print("Tallet inneholder enten 1 eller 7!")
    else:
        print("Tallet inneholder ikke 1 eller 7...")


print("\n"*3)
"""
Oppgave 6 (Utfordring)
https://no.wikipedia.org/wiki/Stein,_saks,_papir

Stein, Saks, Papir

Du skal spille stein, saks, papir mot datamaskinen.
Valget fra datamaskinen er allerde laget for det.
Du må få input fra brukeren.
Sjekk om inputen fra brukeren er ett av alternativene.
Videre må du sjekke om det er enten du eller datamaskinen
som vinner.

Tips: Bruk quit() om inputen fra brukeren ikke er ett av alternativene

"""

print("\nVelkommen til \"Stein, Saks, Papir\"\n")
import random # Ignorer
computer_chose = random.choice(('Stein', 'Saks', 'Papir'))  # Datamaskinen velger en av de tre alternativene

print("Datamaskinen har valgt.\nDet er din tur!")
user_choice = input("Hva velger du: ")
if not user_choice in "Stein Saks Papir":
    print("Feil input!")
    quit()

if user_choice == "Stein" and computer_chose == "Stein":
    print("Uavgjort!\nBegge valgte \"Stein\"")
elif user_choice == "Stein" and computer_chose == "Papir":
    print("Du tapte!\nDatamaskinen valgte \"Papir\" ")
elif user_choice == "Stein" and computer_chose == "Saks":
    print("Du vant!\nDatamaskinen valgte \"Saks\" ")

if user_choice == "Saks" and computer_chose == "Saks":
    print("Uavgjort!\nBegge valgte \"Saks\"")
elif user_choice == "Saks" and computer_chose == "Stein":
    print("Du tapte!\nDatamaskinen valgte \"Stein\" ")
elif user_choice == "Saks" and computer_chose == "Papir":
    print("Du vant!\nDatamaskinen valgte \"Papir\" ")

if user_choice == "Papir" and computer_chose == "Papir":
    print("Uavgjort!\nBegge valgte \"Papir\"")
elif user_choice == "Papir" and computer_chose == "Saks":
    print("Du tapte!\nDatamaskinen valgte \"Saks\" ")
elif user_choice == "Papir" and computer_chose == "Stein":
    print("Du vant!\nDatamaskinen valgte \"Stein\" ")
