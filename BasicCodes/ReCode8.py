sal = int(input("Enter the salary: "))

if(sal<=8000):
    tax = 0.0
elif(sal>8000 and sal<=9000):
    tax = (sal*20)/100
elif(sal>9000 and sal<=10000):
    tax = (sal*30)/100
else:
    tax = (sal*40)/100

print("Salary is: ",sal)
print("Tax is: ",tax)

net = (sal-tax)
print("Net Salary is: ",net)