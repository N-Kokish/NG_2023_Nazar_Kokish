
znak = input("select operation(+,-,*,/,**,!**)")
number_1 = int(input("a = "))
number_2 = int(input("b = "))
match znak :
    case str("+"):
        print("You selected add(a+b=)")
        print("sum "+str(number_1+number_2))
    case str("-"):
        print("You chose subtraction(a-b=)")
        print("difference "+str(number_1-number_2))
    case str("*"):
        print("You chose multiplication(a*b=)")
        print("product "+str(number_1*number_2))
    case str("/"):
        print("You chose division(a/b=)")
        if number_2 != 0 :
         print("fraction "+str(number_1/number_2))
        else:
            print("It is not possible to divide by 0, please choose the second number for repeated division")
    case str("**"):
        print("You chose multiplication(a**b=)")
        print("raised to a power "+str(number_1**number_2))     
    case str("!**"):
        print("You have chosen the operation of the roots of a number(a**1/b=)")
        print("The root of this number "+str(number_1**(1/number_2)))         