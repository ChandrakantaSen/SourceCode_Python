import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

# load IRIS.csv file
df = pd.read_csv('IRISdataset\\Iris.csv')

# Print the entire csv file 
print(df)

# df.head() only shows the first 5 rows from the data set table.
# All the numerical values are in centimeters.
print(df.head())

# Some basic statistical analysis about the data
print(df.describe())

print(df.dtypes)

# Visualize the whole dataset
# To visualize the whole dataset we used the seaborn pair plot method. It plots the whole dataset’s information.
sns.pairplot(df, hue='Class_labels')

