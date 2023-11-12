def print(numbers, dividers):
    print("---" * 18)
    for index, value in enumerate(numbers, start=1):
        dividers_list = [i for i in range(1, value + 1) if value % i == 0]
        print("\n{} | {}".format(index, dividers_list))
        if len(dividers_list) == 2:
            prime_numbers.append(index)
    
   # print("---" * 18)
   # print("Prime numbers: {}".format(prime_numbers))

number = int(input("Введите число: "))
numbers = list(range(1, number + 1))
prime_numbers = []

print(numbers, prime_numbers)