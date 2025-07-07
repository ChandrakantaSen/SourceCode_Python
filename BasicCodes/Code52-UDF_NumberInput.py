# User Defined Function - Without return type, without parameters

def chk_factors():
    n = int(input("Enter the numbers: "))

    for i in range(1,(n+1),1):
    # for(i=1;i<=n;i++)
	    if n % i == 0:
	    	print("Factors are: ",i)

chk_factors()