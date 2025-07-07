import csv
file = open('E:\\StudyWorkspace - I\\Source_Code (Python)\\CSVfiles\\Files\\customer.csv')
reader = csv.reader(file)
for line in reader:
    print(line)