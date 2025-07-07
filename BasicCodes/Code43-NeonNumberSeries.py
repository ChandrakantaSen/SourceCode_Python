#WAP to check a number is Neon or not

n = int(input("Enter the range: "))

i = 1
while(i<=n):
    p = int(i*i)
    sum = 0
    while(p!=0):
        d = int(p % 10)
        sum = sum + d
        p = int(p / 10)
    if(sum == i):
        print(sum,end=" ")  
    i+=1