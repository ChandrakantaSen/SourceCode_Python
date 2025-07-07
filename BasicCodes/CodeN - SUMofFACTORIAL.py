# WAP to print the sum of factorial value till n numbers

n = int(input("Enter the range: "))

def SOF(x):
	sum = 0
	for i in range(1,x+1):
		fact = 1
		for j in range(1,i+1):
			fact = fact * j
		sum = sum + fact
		
	print("required Sum is: ",sum)
	
SOF(n)