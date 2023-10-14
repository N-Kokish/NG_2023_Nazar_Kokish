index = 1
number = int(input("to see how much you want to keep sacred values = "))
lst=[]
while index < (number+1) :
    element = input("leads element {}= ".format(index))
    lst.insert(index, element)
    index=index+1
lst_set=list(set(lst))
print("a list of unique values {}".format(lst_set))