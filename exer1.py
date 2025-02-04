

def double_it():
    numbers = []
    for i in range(5):
        number = int(input("Type the whole numbers for the list (five at least): "))
        numbers.append(number)
    the_double = list(map(lambda x: x*2, numbers))
    print(the_double)
    
double_it()



    