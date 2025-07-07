import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd', 'e'])
s = pd.Series(data, index=[1000, 1001, 1002, 1003, 1004])
print(s)