# WAP to check a number is Factorial or not

n = int(input("Enter the number: "))

f = 1
for i in range(1,(n+1),1):
	f = f * i

print("Factorial is: ",f)

