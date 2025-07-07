sal = int(input("Enter the Salary Amount: "))

if(sal<=20000):
    comm = (sal*3)/100
    print("Salary is: ",sal)
    print("Commission is: ",comm)
    print("commission rate is 3%")
elif(sal>20000 and sal<=50000):
    comm = (sal*12)/100
    print("Salary is: ",sal)
    print("Commission is: ",comm)
    print("commission rate is 12%") 
else:
    comm = (sal*31)/100
    print("Salary is: ",sal)
    print("Commission is: ",comm)
    print("commission rate is 31%")