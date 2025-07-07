# WAP to print the swapped value of two variables (using 3rd variable)
a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

c = a
a = b
b = c

print("Swapped value of a is: ",a)
print("Swapped value of b is: ",b)