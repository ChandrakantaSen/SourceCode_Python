## Creating a DataFrame from a List (1D) - without column header
'''A simple way to create a DataFrame is by using a single list. Pandas automatically assigns index values 
   to the rows when you pass a list.
    * Each item in the list becomes a row.
    * The DataFrame consists of a single unnamed column.
'''
import pandas as pd

lst = ['a','b','c','d']
df = pd.DataFrame(lst)
print(df)