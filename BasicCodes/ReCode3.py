# WAP to print the swapped value of two variables (without using 3rd variable)

a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

a = a + b
b = a - b
a = a - b

# a,b = b,a
print("Swapped value of a is: ",a)
print("Swapped value of b is: ",b)