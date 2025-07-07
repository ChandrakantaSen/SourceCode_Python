## Creating a DataFrame from a List (2D) - with column header

import pandas as pd

lst = [
    ["Bob", "Doe", "bob@example.com"],
    ["Mark", "Markson", "mark@example.com"],
    ["Jane", "Swift", "jane@example.com"],
    ["Patrick", "Johnson", "patrick@example.com"]
]

df = pd.DataFrame(lst, columns=["First Name", "Last Name", "Email"])
print(df)