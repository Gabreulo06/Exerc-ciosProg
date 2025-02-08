

def power_of_two():
    numbers = []
    for i in range(5):
        number = float(input("Type the numbers: (five at maximum): "))
        numbers.append(number)
    in_power_of_two = sorted(map(lambda x: x**2, numbers))
    
    print(in_power_of_two)
    
power_of_two()
        