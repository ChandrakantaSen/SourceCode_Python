import matplotlib.pyplot as plt 
import csv 

x = [] 
y = [] 

with open('E:\\StudyWorkspace - I\\Source_Code (Python)\\CSVfiles\\Files\\TEST.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',') 
	
	for row in plots: 
		x.append(row[0]) 
		y.append(int(row[2])) 

plt.bar(x, y, color = 'g', width = 0.72, label = "Age") 
plt.xlabel('Names') 
plt.ylabel('Ages') 
plt.title('Ages of different persons') 
plt.legend() 
plt.show() 
