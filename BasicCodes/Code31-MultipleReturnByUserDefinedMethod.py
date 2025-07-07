# Multiple value return from user defined method

def getData():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    return num1,num2

def MultipleReturn():
    m,n = getData()
    print(" ", m, " ", n)


MultipleReturn()
