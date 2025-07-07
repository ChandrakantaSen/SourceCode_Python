# WAP to calculate the no of vowels and consonant of a string
str = input("Enter the String: ")
l = len(str)

vwl = 0
cons = 0
spc = 0
for i in range(0,l):
    ch = str[i]
    if(ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U" or ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        vwl = vwl + 1
    else:
        if(ch == " "):
            spc = spc + 1
        else: 
            cons = cons + 1

print("No of Vowels is: ",vwl)
print("No of Consonent is: ",cons)
print("No of Space is: ",spc)

