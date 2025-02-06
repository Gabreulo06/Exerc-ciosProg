
from functools import reduce

def somatory():
    numbers = []
    for i in range(5):
        number = int(input("Insert the whole numbers (five at maximum): "))
        numbers.append(number)
    total = reduce(lambda x, y: x + y, numbers)
    print(f"The somatory of the numbers is: {total}")

somatory()
        