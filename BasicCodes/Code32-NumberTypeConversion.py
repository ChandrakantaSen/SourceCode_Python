# Program for Number Type Conversion

def getData():
    m = int(input("Enter number1: "))
    n = float(input("Enter number2: "))
    return m,n

def Calc():
    p,q = getData()
    print("Integer Number is: ",int(p))
    #print("Long Number is: ",long(q))
    print("Float Number is: ",float(q))
    print("Complex Number is: ",complex(p))
    print("Complex Number is: ",complex(p,q))

Calc()
