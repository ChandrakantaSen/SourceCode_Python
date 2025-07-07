# WAP to print the words from a string
str = input("Enter the String: ")
str = str + " "
l = len(str)
wrd = ""
for i in range(0,l):
    ch = str[i]
    if(ch != " "):
        wrd = wrd + ch
    else:
        print(wrd)
        wrd = ""