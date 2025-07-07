#WAP to find the Prime factors of a number

n = int(input("Enter the number: "))

i = 1

while(i<=n):
    if(n%i==0):
        c = 0
        for j in range(1,i+1,1):
            if(i%j==0):
                c+=1
        if(c==2):
            print(i,end=" ")
    i+=1