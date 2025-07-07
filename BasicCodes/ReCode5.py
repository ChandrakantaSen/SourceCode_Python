# WAp to find the factorial value of a number

n = int(input("Enter the number: "))

i=1
prod = 1
while(i<=n):
    prod = prod * i
    i+=1

print("Value is: ",prod)