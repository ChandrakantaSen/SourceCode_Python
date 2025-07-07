# WAP to user input of the array elements
import array as p
arr = []
n = int(input("Enter the number of elements: "))

for i  in range(n):
    v = int(input("Element: "))
    arr.append(v)

print(arr)