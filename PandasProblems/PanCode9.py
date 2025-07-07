## Creating an Empty DataFrame and Adding Columns from Lists

import pandas as pd

df = pd.DataFrame()
df['First Name'] = ["Bob", "Mark", "Jane", "Patrick"]
df['Age'] = [32, 25, 41, 29]

print(df)