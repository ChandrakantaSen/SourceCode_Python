# WAP to user input elements in a NumPy array
import numpy as np
arr = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    v = input("Element:  ")
    arr.append(float(v))

p = np.array(arr)
print(p)
