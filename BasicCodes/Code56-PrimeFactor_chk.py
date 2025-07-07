# WAP to find the prime factors of a number

n = int(input("Enter the numbers: "))

def chkPrime(x):
    c = 0
    for i in range(1,x+1):
        if(x % i == 0):
            c+=1
    if(c == 2):
        return 0
    else:
        return 1

def chkFactor(n):
    for i in range(1,n+1):
        if(n % i == 0):
            val = chkPrime(i)
            if(val == 0):
                print("Prime Factors are: ",i)

chkFactor(n)