#WAP to  print the non Fibonacci Series

n = int(input("Enter the number: "))

f0=0;f1=1
for i in range(1,(n+1),1):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    #print(f2,end=" ")
    f3 = f0 + f1
    for x in range(f2+1,f3,1):
        if(x<=n):
            print(x,end=" ")        
        else:
            break