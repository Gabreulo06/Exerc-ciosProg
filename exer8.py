
from functools import reduce

def word_list():
    
    
    list_of_words = []
    
    for i in range(5):
        
        words = str(input("Write five words: "))
        list_of_words.append(words)
    
    letters_number = list(map(len, list_of_words))
    somatory = reduce(lambda x, y: x + y, letters_number)
    
    print(somatory)

word_list()
    
        
        