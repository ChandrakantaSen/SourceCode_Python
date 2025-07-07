# Distance Travelled as per the Tariff (Bus Fare Problem)

dist = int(input("Enter the distance travelled: "))

if dist <= 10:
    charge = 80.00
elif dist > 10 and dist <= 20:
    charge = 80.00 + (dist - 10)*6
elif dist > 20 and dist <= 30:
    charge = 80.00 + 60.00 + (dist - 20)*5
else:
    charge = 80.00 + 60.00 + 50.00 + (dist - 30)*4

print("Bus Fare Charge is: ", charge)
