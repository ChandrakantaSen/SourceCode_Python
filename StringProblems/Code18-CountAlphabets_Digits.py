# WAP to accept a string and print the no. of digits, alphabets and special characters in the screen.
str = input("Enter the String: ")
l = len(str)
c = d = s = 0
for i in range(0,l):
    ch = str[i]
    if(ch >= 'a' and ch <= 'z'):
        c+=1
    elif((ord(ch) - ord('0')) >= 0 and (ord(ch) - ord('0')) <= 9):
        d+=1
    else:
        s+=1
print("No. of Alphabets: ",c)
print("No. of Digits: ",d)
print("No. of Special Characters: ",s)