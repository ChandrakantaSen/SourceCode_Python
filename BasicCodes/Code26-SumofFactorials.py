# Print the sum of factorials of a given range

def getData():
    n = int(input("Enter number1: "))
    return n

def factorial(x):
    f = 1
    for i in range(1,(x+1),1):
        f = f * i
    return f

def sumFactorial():
    rng  = getData()
    sum1 = 0
    for i in range(1,(rng+1),1):
        part = factorial(i)
        sum1 = sum1 + part
    print("Sum is: ", sum1)


    
sumFactorial()
