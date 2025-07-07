n =int(input("Enter the number: "))
temp = n
c=0
for i in range(1,temp+1):
	if(temp % i == 0):
		c+=1
    
if(c==2):
    rev=0
    while(temp!=0):
        d= temp%10
        rev = rev*10+d
        temp=temp//10
		
    d=0
    for j in range(1,rev+1):
        if(rev % j == 0):
            d+=1	
		
    if(d==2):
        print("Twisted Prime")
    else:
        print("Not a Twisted Prime")
else:
    print("Composite Number")