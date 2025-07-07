# WAP to find the Sum of Elements of a numPy array
import numpy as np
arr = []
sum = 0
n = int(input("Enter the number of elements: "))

for i in range(n):
    v = input("Element:  ")
    arr.append(float(v))
p = np.array(arr)

l = len(p)
for i in range(l):
    sum = sum + p[i]
print("Sum of elements is: ",sum)