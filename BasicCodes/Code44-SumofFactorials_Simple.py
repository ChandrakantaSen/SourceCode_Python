# WAP to find the Sum of Factorials of the range

n = int(input("Enter the range: "))

sum1 = 0

for i in range(1,(n+1)):
    fact = 1
    for j in range(1,(i+1)):
        fact = fact * j
    sum1 = sum1 + fact

print("Sum of Factorials is: ",sum1)
    
