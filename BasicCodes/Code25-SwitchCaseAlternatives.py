# Switch Case Alternatives

import sys
ch = int(input("Enter the choice: "))

def exitSystem():
    sys.exit()

def addition():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    sum1 = (num1 + num2)
    print("Required Sum is: ", sum1)

def subtraction():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    diff = (num1 - num2)
    print("Required Difference is: ", diff)

def multiplication():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    mul = (num1 * num2)
    print("Required Multiplication is: ", mul)

def division():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    div = (num1 / num2)
    print("Required Division is: ", div)

def modulodivision():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    mod = (num1 % num2)
    print("Required Modulo Division is: ", mod)

def switchCase(c):
    if(c == 0):
        exitSystem()
    elif(c == 1):
        addition()
    elif(c == 2):
        subtraction()
    elif(c == 3):
        multiplication()
    elif(c == 4):
        division()
    elif(c == 5):
        modulodivision()    

        
switchCase(ch)

