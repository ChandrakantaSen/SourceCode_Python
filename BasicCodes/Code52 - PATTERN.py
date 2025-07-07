# WAP to draw the PATTERN -
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def pattern():
	for i in range(1,5):
		for j in range(1,i+1):
			print(j,' ')
		print("\n")
		
pattern()
