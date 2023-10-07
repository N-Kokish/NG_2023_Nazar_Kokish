
znak = input("select operation(+,-,*,/,**,!**)")
match znak :
    case str("+"):
        print("You selected add(a+b)")
        a = int(input("a = "))
        b = int(input("b = "))
        print("sum "+str(a+b))
    case str("-"):
        print("You chose subtraction(a-b)")
        a = int(input("a = "))
        b = int(input("b = "))
        print("difference "+str(a-b))
    case str("*"):
        print("You chose multiplication(a*b)")
        a = int(input("a = "))
        b = int(input("b = "))
        print("product "+str(a*b))
    case str("/"):
        print("You chose division(a/b)")
        a = int(input("a = "))
        b = int(input("b = "))
        if b != 0 :
         print("fraction "+str(a/b))
        else:
            print("It is not possible to divide by 0, please choose the second number for repeated division")
    case str("**"):
        print("You chose multiplication(a**b)")
        a = int(input("a = "))
        b = int(input("b = "))
        print("raised to a power "+str(a**b))     
    case str("!**"):
        print("You have chosen the operation of the roots of a number(a**1/b)")
        a = int(input("a = "))
        b = int(input("b = "))
        print("The root of this number "+str(a**(1/b)))         