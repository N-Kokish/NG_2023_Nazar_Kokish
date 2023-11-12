
znak = input("select operation(+,-,*,/,**,!**)")
number_1 = int(input("a = "))
number_2 = int(input("b = "))
match znak :
    case str("+"):
        print((number_1+number_2))
    case str("-"):
        print((number_1-number_2))
    case str("*"):
        print((number_1*number_2))
    case str("/"):
        if number_2 != 0 :
         print((number_1/number_2))
        else:
            print("It is not possible to divide by 0, please choose the second number for repeated division")
    case str("**"):
        print((number_1**number_2))    
    case str("!**"):
        print((number_1**(1/number_2)))         