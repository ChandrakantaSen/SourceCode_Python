#Largest prime factor - The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

n = int(input("Enter the number: "))

max=0
for i in range(1,(n+1),1):
    if(n%i==0):
        temp=i
        c=0
        for j in range(1,(temp+1),1):
            if(temp%j==0):
                c+=1
        if(c==2):
            if(max<i):
                max=i
print(max)