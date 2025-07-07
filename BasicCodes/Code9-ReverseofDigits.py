# Reverse of digit

num = int(input("Enter the number: "))

d1 = (num % 10)
d2 = (num / 10) % 10
d3 = (num / 100)

rev = int(d1 * 100 + d2 * 10 + d3 * 1)
# print (int(d1)*100)
# print (int(d2)*10)
# print (int(d3)*1)
print("Sum of digit: ",rev)
