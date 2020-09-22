"""
Oppgave 1

Lag en liste av tupler fra de to gitte listene.
"""

lst1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2 = ["Oslo", "Bergen", "Trondheim", "Bodø", "Stavanger", "Molde"]
lst_of_tuples = list(zip(lst1, lst2))
print(lst_of_tuples)

"""
Oppgave 2

Lag en dictionary fra de to gitte listene.
"""

lst1 = [123, 321, 213, 312]
lst2 = ["Netflix", "HBO", "Dplay", "Viaplay"]
dict1 = dict(zip(lst1, lst2))
print(dict1)


"""
Oppgave 3
Lag en sortert liste av tuples av de to gitte listene.

"""

lst1 = ["Karoline", "Simon", "Vilde", "Tiril"]
lst2 = [4, 12, 7, 19]
lst1.sort()
lst2.sort()
lst = list(zip(lst1, lst2))
print(lst)

