# Star Pattern - 1 -- Pascal's Triangle
n = int(input("Enter the number: "))
for i in range(1,n+1):
      for j in range(n-i):
         print(' ', end='')

      C = 1
      for j in range(1, i+1):
         print(C, ' ', sep='', end='')
         C = C * (i - j) // j
      print()