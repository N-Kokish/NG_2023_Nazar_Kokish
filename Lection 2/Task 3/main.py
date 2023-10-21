def pop():
    print("---"*18)
index = 1
number = int(input("to see how much you want to keep sacred values = "))#the number entered by the use
lst=[]
lst_prime_numbers=[]
lst_dividers=[]
numbers=0
while index < (number+1) :#entry of numbers from 1 to the number entered by the user in the list
    numbers = numbers+1
    lst.insert(index, numbers)
    index=index+1
index=0
while index<len(lst):
    for i in range(1, int(len(lst)+1)):
     if (lst[index]) % i == 0:
        lst_dividers.append(i)
    print("\n{} | ".format(index+1),lst_dividers)
    if int(len(lst_dividers)) == 2:
       lst_prime_numbers.append(index+1)
    lst_dividers.clear()
    index=index+1 
pop()
print("Prime numbers: {}".format(lst_prime_numbers) )      