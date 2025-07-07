# Print the HCF and LCM of two input numbers

def getData():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    return num1,num2

def HCF_LCM():
    m,n = getData()
    p = m*n
    for i in range(1,p,1):
        if m % i == 0 and n % i == 0:
            h = i
    l = p/h    
    print("HCF is: ",h)
    print("LCM is: ",l)


HCF_LCM()
