
def pair_numbers():
    numbers = []
    for i in range(5):
        number = int(input("Type five whole numbers: "))
        numbers.append(number)
    the_pairs = list(filter(lambda x: x % 2 == 0, numbers))
    print(the_pairs)
    
pair_numbers()
        
        