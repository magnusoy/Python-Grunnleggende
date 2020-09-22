"""
Oppgave 1

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

results1 = count_sevens(1, 4, 7)
results2 = count_sevens(*numbers)
print(results1)
print(results2)


"""
Oppgave 2

Du skal lage en funksjon calculate som aksepterer en liste av nøkkelord argument:

make_float, en boolean som returnerer en float hvis True, eller en int hvis False
operation, som er enten "add", "subtract", "multiply" eller "divide"
first, som er et tall
second, som er et annet tall

Funksjonen skal returnerer resultatet av å kjøre akkurat det du legger inn.
Altså gjøre den nevnte operasjonen med det første og andre tallet.
Husk at make_float bestemmer om det returneres en float eller int.

Eks.
calculate(make_float=False, operation="add", first=2, second=4) -> 6
calculate(make_float=True, operation="divide", first=3.5, second=5) -> 0.7
"""

def calculate(**kwargs):
    operation_lookup = {
        "add": kwargs.get("first", 0) + kwargs.get("second", 0),
        "subtract": kwargs.get("first", 0) - kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) / kwargs.get("second", 0),
        "multiply": kwargs.get("first", 0) * kwargs.get("second", 0)
    }
    is_float = kwargs.get("make_float", False)
    operation_value = operation_lookup[kwargs.get("operation", "")]
    if is_float:
        final = float(operation_value)
    else:
        final = int(operation_value)
    return final

print(calculate(make_float=False, operation="add", first=2, second=4))
print(calculate(make_float=True, operation="divide", first=3.5, second=5))