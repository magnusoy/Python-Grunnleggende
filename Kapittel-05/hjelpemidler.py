# Hjelpemidler for å løse oppgaver i kapittelet

# For loop -> 0 - 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in range(11):
    print(i)

# For loop -> 0 - 10, øker med 2 om gangen (0, 2, 4, 6, 8, 10)
for i in range(0, 11, 2):
    print(i)

# Itererer gjennom teksten ( U t d a n n e t . n o)
txt = "Utdannet.no"
for index in range(len(txt)):
    elemenet = txt[index]
    print(elemenet)

# Itererer gjennom teksten ( U t d a n n e t . n o)
for char in txt:
    print(char)

# Itererer gjennom teksten ( U t d a n n e t . n o)
index = 0
while index < len(txt):
    element = txt[index]
    print(elemenet)
    index += 1

# Itererer gjennom teksten. Sier fra når den finner .
# (U t d a n n e t Fant: . . n o)
for char in txt:
    if char == ".":
        print("Fant: .")
    print(char)

# Itererer gjennom teksten men avslutter ved .
# (U t d a n n e t)
for char in txt:
    if char == ".":
        break
    print(char)

# Itererer gjennom teksten men hopper over ved .
# (U t d a n n e t n o)
for char in txt:
    if char == ".":
        continue
    print(char)
