# WAP to print the reverse of a number

n = int(input("Enter the number: "))

def ROD(x):
	
	rev = 0
	while(x!=0):
		d = x % 10
		rev = rev * 10 + d
		x = x / 10
	print("Reverse Number is: ",rev)


ROD(n);
