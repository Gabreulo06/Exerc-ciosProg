

def name_list():
    names = []
    for i in range(5):
        name = str(input("Type the names (five at maximum): "))
        names.append(name)
    long_names = list(filter(lambda x: len(x) > 5, names))
    
    print(long_names)
      
name_list()
        
    