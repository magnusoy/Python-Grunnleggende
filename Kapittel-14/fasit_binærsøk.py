import random

def binary_search(lst, number):
    """
    docstring
    """

    low = 0
    high = len(lst) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if number is present at mid 
        if lst[mid] < number: 
            low = mid + 1
        # If number is greater, ignore left half 
        elif lst[mid] > number: 
            high = mid - 1
        # If number is smaller, ignore right half 
        else: 
            return mid 
    # If we reach here, then the element was not present 
    return -1


numbers = random.sample(range(1, 50), 45)
print(numbers)
print(binary_search(numbers, 12))