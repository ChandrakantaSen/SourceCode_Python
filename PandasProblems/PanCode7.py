## Creating a DataFrame from Multiple Lists Using zip()
import pandas as pd

first_names = ["Bob", "Mark", "Jane", "Patrick"]
last_names = ["Doe", "Markson", "Swift", "Johnson"]

df = pd.DataFrame(list(zip(first_names, last_names)), columns=["First Name", "Last Name"])
print(df)