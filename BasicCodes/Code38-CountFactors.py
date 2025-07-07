#WAP to count the factors of a number

n = int(input("Enter the number: "))

c = 0
for i in range(1,(n+1),1):
	if n % i == 0:
		c+=1
		
print("The Count of the Factors are: ",c)		
