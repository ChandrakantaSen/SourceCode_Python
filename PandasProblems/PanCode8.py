## Using pd.DataFrame.from_records()
'''
    We can also use from_records() to create a DataFrame from a list of tuples or lists
'''
import pandas as pd

data = [
    ("Bob", "Doe", "bob@example.com"),
    ("Mark", "Markson", "mark@example.com"),
    ("Jane", "Swift", "jane@example.com"),
    ("Patrick", "Johnson", "patrick@example.com")
]

df = pd.DataFrame.from_records(data, columns=["First Name", "Last Name", "Email"])
print(df)