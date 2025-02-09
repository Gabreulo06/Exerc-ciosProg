

def pair_and_odd(numbers, pair, odd):
    numbers.append({"pair numbers": pair, "odd numbers:": odd}) 
    
def main():
    numberlist = []
    
    for i in range(8):
        gen_numbers = int(input("Type the whole numbers (eight at maximum): "))
        numberlist.append(gen_numbers)

        
    separate_numbers1 = list(filter(lambda x: x % 2 == 0, numberlist))
    separate_numbers2 = list(filter(lambda x: x % 2 != 0, numberlist))
    
    pair_and_odd(numberlist, separate_numbers1, separate_numbers2)
    
    print("Numbers: ", numberlist)
    
main()

  

    

    
    
        
        
    
    