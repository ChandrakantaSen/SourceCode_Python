# UDF: Without return type and also with parameters

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def sum2nos(x,y):
    z = (x + y)
    print("Sum is: ",z)

sum2nos(a, b)