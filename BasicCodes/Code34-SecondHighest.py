# Example of if-elseif program
n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
n3 = int(input("Enter the number3: "))


if(n1>n2):
    if(n1>n3):
        if(n2>n3):
            maxV = n2
        else:
            maxV = n3
elif(n2>n1):
    if(n2>n3):
        if(n1>n3):
            maxV = n1
        else:
            maxV = n3
elif(n3>n1):
    if(n3>n2):
        if(n1>n2):
            maxV = n1
        else:
            maxV = n2
else:
    print "All are equal..."

print maxV
