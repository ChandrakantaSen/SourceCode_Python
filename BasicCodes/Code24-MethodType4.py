# Method Type3: With return and also with parameters
a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))
c = int(input('Enter Third number : '))

# method definition
def maxof2nos(x,y,z):
    
    if(x > y and x > z):
        max1 = x
    elif(y > x and y > z):
        max1 = y
    else:
        max1 = z
    return max1
    


# method calling
result = maxof2nos(a,b,c)
print("Maximum of 3 nos.: ",result)

