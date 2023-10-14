index = 0
number = int(input("to see how much you want to keep sacred values = "))
lst_numbers=[]
while index < (number) :
    element = input("leads element {}= ".format(index+1))
    if element.isdigit():
      lst_numbers.insert(index, element)  

    index=index+1
print("The following numbers were entered: {}".format(lst_numbers))