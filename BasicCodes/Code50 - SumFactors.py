# Print the factors
n = int(input("Enter the number: "))

i=1
sum=0
while(i<=n):
    if(n%i==0):
        print(i,end=" ")
        sum = sum + i
    i+=1

print("\nSum of Factors are: ", sum)