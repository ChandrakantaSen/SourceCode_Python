# Write a program to input a string in uppercase and print the frequency of each character.
str = input("Enter the String: ")
str += " "
length = len(str)
count = 0
for i in range(0,length):
    ch = str[i]
    for j in range(97, 123):
        if(ch == chr(j)):
            count+=1
    if(count > 0):
        print("Character is: ",ch,"---- Frequency is: ",count)
        count = 0