## Creating a DataFrame from a List (1D) - with column header
import pandas as pd

lst = ["Bob", "Mark", "Jane", "Patrick"]
df = pd.DataFrame(lst, columns=["First Name"])

print(df)