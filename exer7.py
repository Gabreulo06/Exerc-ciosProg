

def number_types_dic(lib, positive, negative, nule):
    lib.append({"positive numbers": positive, "negative numbers": negative, "zeros": nule})
    
def main():
    
    gen_numbers = []
    
    for i in range(8):
        
        numbers = int(input("Type the whole numbers (eigth at maximum): "))
        
        gen_numbers.append(numbers)
        
    positive_inputs = list(filter(lambda x: x > 0, gen_numbers))
    negative_inputs = list(filter(lambda x: x < 0, gen_numbers))
    zero_inputs = list(filter(lambda x: x == 0, gen_numbers))
    number_types_dic(gen_numbers, positive_inputs, negative_inputs, zero_inputs)
        
    print(gen_numbers)
        
main()   # Nesse caso, não há necessidade do uso de 'map'.
        
        
            
    
    