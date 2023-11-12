import json
import collections
lst=[]
text = str(input("enter a file name : "))
with open(text, "r") as f:
    for number_of_terms in f.readlines():
        for symbols in number_of_terms:
          lst.append(symbols)  
          print(lst)
number_of_each_character = collections.Counter(lst)#considers each element separately (as if a line or a word or a symbol)+ container is a subspecies of the Dictionary class
print(number_of_each_character)
print ("symbol : quantity")
print (json.dumps(number_of_each_character,indent=4))
