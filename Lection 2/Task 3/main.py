def pop():
    print("---"*18)
index = 1
number = int(input("to see how much you want to keep sacred values = "))#число який вів користувач
lst=[]
l=[]
p=0
dilnik=1
numbers=0
numb_dilniki=0
while index < (number+1) :#запись чисел от 1 до числа який вів користувач
    numbers = numbers+1
    lst.insert(index, numbers)
    index=index+1
print(lst)
for element_given in lst:#вивод списка в стовпчик
    print(element_given)
index=0
while index<len(lst):
    for i in range(1, int(len(lst))):
     if (lst[index]) % i == 0:
        print(str(i)+"  индексс {}".format(index))
        l.append(i)
        print(l)
    l.clear()
    index=index+1    