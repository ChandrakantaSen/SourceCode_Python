def getData():
    rng = int(input("Enter range: "))
    return rng

def fibonacciSeries():
    n = getData()
    #print(" ", n)
    f0 = 0
    f1 = 1
    for i in range(0,n,1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        print(" ", f2)


fibonacciSeries()
