# Harshad/Niven Number: It is an integer that is divisible by the sum of its digits.
# For example: 18 -- Sum of digit(18) = 1+8 = 9 and 18 is divisible by 9

n = int(input("Enter the number: "))

temp = n
sum = 0
while(temp != 0):
    d = temp % 10
    sum = sum + d
    temp = temp // 10

print(sum)
if(n % sum == 0):
    print("Harsad Number")
else:
    print("Not a Harsad Number")