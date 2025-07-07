#WAP to check a number is Weakarm or not

n = int(input("Enter the number: "))

temp = n; sum = 0; c = 0;

while(temp != 0):
	temp = int(temp / 10)
	c += 1

temp = n
#print(c)

while(temp != 0):
	d = int(temp % 10)
	sum = sum + d**c
	c-=1
	temp = int(temp / 10)
	
if sum == n:
	print("Weakarm Number")
else:
	print("Not a Weakarm Number")

