a = input("Enter the string value: ")
b = input("Enter the string value: ")
c = input("Enter the string value: ")

if(a > b == True and a > c == True):
    if(b > c == True):
        max = b
    else:
        max = c
elif(b > a == True and b > c == True):
    if(a > c == True):
        max = a
    else:
        max = c
elif(c > a == True and c > b == True):
    if(a > b == True):
        max = a
    else:
        max = b
else:
    print("All are equal...")

print("Second Largest Value is: ",max)
