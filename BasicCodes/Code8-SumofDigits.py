# Sum of digit

num = int(input("Enter the number: "))

d1 = (num % 10)
d2 = (num / 10) % 10
d3 = (num / 100)

sum = int(d1 + d2 + d3)
print("Sum of digit: ",sum)
