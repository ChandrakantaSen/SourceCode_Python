# WAP to print the composite series upto n terms

n = int(input("Enter the range: "))

for i in range(1,(n+1)):
    temp = i
    c=0
    for j in range(1,(temp+1)):
        if(temp%j == 0):
            c+=1
    if(c>2):
        print(temp,end=" ")