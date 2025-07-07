# Print the range of primes

def getData():
    n = int(input("Enter number: "))
    return n

def primeRange():
    rng = getData()
    count = 0
    for i in range(1,(rng+1),1):
        for j in range(1,(i+1),1):
            if(i % j == 0):
                count += 1
        if(count == 2):
            print(" ",i)
        count = 0
    
primeRange()
