# Lage en dictionary
dct = dict()
print(dct)

# Lage en dictionary
dct = {}
print(dct)

# Lage en dictionary
dct = dict(Navn="Magnus", Alder=25)
print(dct)

# Lage en dictionary
dct = {"Navn": "Magnus", "Alder": 25}
print(dct)

# Hente ut verdi
name = dct["Navn"]
print(name)

# Sjekk om en nøkkel finnes i dictinary
print("Navn" in dct)

# Sjekk om en nøkkel finnes i dictinary
if "Navn" in dct:
    print("Ja det gjør den")

# Kopier dictionary
dct2 = dct.copy()
print(dct2)

# Legge til en ny nøkkel med None verdi
dct2.setdefault("By")
print(dct2)

# Legge til en ny nøkkel med string verdi
dct2.setdefault("Land", "Norge")
print(dct2)

# Fjerne nøkkel og verdi fra dictionary
dct2.pop("By")
print(dct2)

