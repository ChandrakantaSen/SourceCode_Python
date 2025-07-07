# Write a program to input a sentence and print each word of the string along with its length in tabular form.
str = input("Enter the String: ")
str += " "
length = len(str)
wrd = ""
for i in range(0,length):
    ch = str[i]
    if(ch != " "):
        wrd = wrd + ch
    else:
        l = len(wrd)
        print(wrd,"-----",l)
        wrd = ""
        l = 0