#Largest Palindrome Product

n = int(input("Enter the number: "))

#palindrome checking
def chkPalindrome(x):
    temp = x
    rev = 0
    while(temp!=0):
        d = int(temp % 10)
        rev = int(rev * 10 + d)
        temp = int(temp / 10)
    
    if(rev == x):
        return 0
    else:
        return 1

#maximum checking
def chkMax(x):
    max1 = 0
    if(max1 < x):
        max1 = x
    return max1

#palindrome series generate
def showPalinSeries():
    for i in range(1,(n+1),1):
        p = chkPalindrome(i)
        if(p == 0):
            q = chkMax(i)
    print(q,end='')


showPalinSeries()