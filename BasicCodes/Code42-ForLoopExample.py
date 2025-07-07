# For Loop Example

n = int(input("Enter the range: "))
sum = 0
for i in range(0,n):
    print(i, end=" ")
    sum = sum + i

print("\nSum is: ",sum)
