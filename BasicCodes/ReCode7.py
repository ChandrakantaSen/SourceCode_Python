'''
The telephone department wishes to compute monthly telephone bills for its customers using the following rules. Minimum Rs. 250 for first 80 message units, plus 60 paise per unit for next 60 units, plus 50 paise per unit for next 60 units, plus 40 paise per unit for any units above 200. Write a program that calculates the monthly bill, with input MESSAGE (the number of message units) and CUSTNO (the registration number of a customer). Then Display the bill in following format.
            CUSTOMER NO:
            MESSAGE UNITS:
            AMOUNT (Rs.):
'''
c = input("Enter the Customer No.: ")
n = int(input("Enter the units: "))

if(n<=80):
  bill = 250.00
elif(n>80 and n<=140):
  bill = 250 + (n-80)*0.60
elif(n>140 and n<=200):
  bill = 250 + 36 + (n-140)*0.50
else:
  bill = 250 + 36 + 30 + (n-200)*0.40

print("\n\n=============================");
print("Customer No.: ", c)
print("Consumed Electricity Units: ", n)
print("Bill Amount: ", bill)