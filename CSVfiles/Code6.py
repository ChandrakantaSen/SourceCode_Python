# File Handling - Read CSV file using CSV module
import csv
file = open('E:\\StudyWorkspace - I\\Source_Code (Python)\\CSVfiles\\Files\\username.csv')
reader = csv.reader(file)
for line in reader:
    print(line)