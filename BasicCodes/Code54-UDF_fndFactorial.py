#UDF - With return type, without parameters

def fndFactorial():
    n = int(input("Enter the number: "))

    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
    

val = fndFactorial()
print("Fctorial is: ",val)