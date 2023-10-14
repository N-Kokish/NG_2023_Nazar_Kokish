print("Conversion from Celsius to Fahrenheit and vice versa")
perevod= int(input("Enter 0 if you need to convert from Celsius to Fahrenheit or enter 1 if vice versa: "))
#temp= float(input(""))
def Temp_print():
     return float(input("lead, please: "))
    
if perevod == 0  :
    print("Celsius-->Fahrenheit")
    print("Fahrenheit="+str(Temp_print()*1.8+32))
if perevod == 1 :
    print("Fahrenheit-->Celsius")
    print("Celsius="+str((Temp_print()-32)/1.8))
if perevod != 1 and perevod != 0  :
    print("ERROR .The mistake was that you did not enter 1 or 0, but some other number")
