print("Enter a, b, c according to the pattern to solve the quadratic equation:a*x^2+b*x+c=0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b**2-4*a*c
if D == 0 :
    x1 = (-b)/(2*a)
    print("x = "+str(x1))
if D > 0 :
    x1= ((-b +D**(1/2))/(2*a))
    x2= ((-b -D**(1/2))/(2*a))
    print("x1 = "+str(x1))
    print("x2 = "+str(x2))
if D < 0 :
    print("x1 = "+str((-b)/(2*a))+"+"+str(((-D)**(1/2))/(2*a))+"*i")
    print("x2 = "+str((-b)/(2*a))+"-"+str(((-D)**(1/2))/(2*a))+"*i")