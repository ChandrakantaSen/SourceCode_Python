# WAP to find the value of sum of digits on any number

def SOD():
	n = int(input("Enter the number: "))
	
	sum = 0
	while(n!=0):
		d = n%10
		sum = sum + d
		n = n/10;
		
	print("Sum is: ",sum)
	
	
SOD()