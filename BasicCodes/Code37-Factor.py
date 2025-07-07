# WAP to check the factors of a number

n = int(input("Enter the number: "))

for i in range(1,(n+1),1):
	if n % i == 0:
		print("Factors are: ",i)
