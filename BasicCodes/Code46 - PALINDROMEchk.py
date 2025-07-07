# WAP to check a number is PALINDROME or not
n = int(input("Enter the number: "))

def palindromeCHK(x):
	test = x
	rev = 0
	while(test != 0):
		d = test % 10
		rev = rev * 10 + d
		test = test // 10

	if(rev == x):
		print("Palindrome Number")
	else:
		print("Not a Palindrome Number")
		
palindromeCHK(n)