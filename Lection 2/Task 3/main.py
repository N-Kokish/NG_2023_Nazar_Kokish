def pop():
    print("---"*18)
index = 1
number = int(input("to see how much you want to keep sacred values = "))#число який вів користувач
lst=[]
l=[]
numbers=0
numb_dilniki=0
while index < (number+1) :#запись чисел от 1 до числа який вів користувач
    numbers = numbers+1
    lst.insert(index, numbers)
    print(lst)
    index=index+1
for element_given in lst:#вивод списка в стовпчик
    print(element_given)
pop()