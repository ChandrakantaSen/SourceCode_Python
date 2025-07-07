#WAP to check a number is Armstrong or not

n = int(input("Enter the number: "))

temp = n
sum = 0

while (temp != 0):
	d = int(temp % 10)
	sum = sum + int(d*d*d)
	temp = int(temp / 10)

if sum == n:
	print("Armstrong Number")
else:
	print("Not Armstrong Number")
