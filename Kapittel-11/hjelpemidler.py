# Lambda funksjon
square = lambda x: x**2
print(square(2))

# Lambda funksjon
a = 3
result = (lambda x: x + 1)(a)
print(result)

# Lambda funksjon 
full_name = lambda first, last: f'Full name: {first.upper()} {last.upper()}'
print(full_name("Magnus", "Øye"))

# Map
def myfunc(n):
    return len(n)
x = map(myfunc, ('Apple', 'Banana', 'Ananas')) 
print(x)

# Filter
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myFunc, ages)
print(adults)

# Any 
tup = (0, 1, False)
x = any(tup)
print(x)

# All
lst = [True, True, True]
x = all(lst)
print(x)

# Min
x = min(5, 10) 
print(x)

# Max
x = max(5, 10) 
print(x)

# Abs
x = abs(-12)
print(x)

# Round
num = 134.234 / 4.5246
print(num)
print(round(num, 1))

# Lage Zip
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
result = zip(number_list, str_list)
result_set = set(result)
print(result_set)

# Lage Zip
coordinates = ['x', 'y', 'z']
values = [3, 4, 5]
result = zip(coordinates, values)
result_list = list(result)
print(result_list)

# Zip iterering
for i, j in zip(coordinates, values):
    print(f"{i} : {j}")

# lage Enumerate
groceries = ['bread', 'milk', 'butter']
enum_groceries = enumerate(groceries)
print(list(enum_groceries))

# Enumerate
enum_groceries = enumerate(groceries)
for element in enumerate(groceries):
    print(element)

# Enumerate iterering
for count, element in enumerate(groceries):
    print(count, element)

# Enumerate iterering med offset
for count, element in enumerate(groceries, 100):
    print(count, element)