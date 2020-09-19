"""
Oppgave 1
Datamaskinen vil plukke ut en tilfedlig matvare.
Din oppgave er å sjekke om matvaren datamskinen har
plukke ut er kjøleskapet.

Hvis kjøeskapet inneholder matvaren så skal du printe ut antallet.
Om matvaren ikke finnes i kjøleskapet så skal du printe ut at 
kjøleskapet inneholder ikke denne matvaren.

"""

from random import choice

food = choice(["Ost", "Melk", "Rømme", "Salami", "Agurk"])

fridge = {
    "Skinke" : 4,
    "Agurk": 1,
    "Rømme": 2,
    "Paprika": 2,
    "Melk": 2
}

"""
Oppgave 2
Tenk deg at vi lager et dataspill og skal initialisere spilleren i starten.
Med det har jeg en liste med spillegenskaper.

Din oppgave er å generere en dictionary som bruker elementene
i listen som nøkler.
Alle verdiene kan bli initialisert til 0.
"""

game_properties = ["current_score", "high_score", "number_of_lives", 
                    "items_in_inventory", "power_ups", "ammo", 
                    "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", 
                    "minutes_played", "notifications", "achievements"]



"""
Oppgave 3

Vi har et varelager med bakeverk.

1) Lag en kopi av varelageret og kall det stock_list
2) Legg til verdien 18 under nøkkel "Kjeks"
3) Fjern "Kake fra stock_list
"""

inventory = {'Brød': 19, 'Rundstykke': 4, 'Muffins': 8, 'Kake': 1}