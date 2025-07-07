# Method Type2: Without return and also without parameters

# method definition
def maxof2nos():
    x = int(input('Enter First number : '))
    y = int(input('Enter Second number : '))
    z = int(input('Enter Third number : '))

    if(x > y and x > z):
        max1 = x
    elif(y > x and y > z):
        max1 = y
    else:
        max1 = z
    print("Maximum of 3 nos.: ",max1)


# method calling
maxof2nos()
