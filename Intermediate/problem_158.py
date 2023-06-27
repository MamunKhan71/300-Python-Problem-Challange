# Problem 158
# Write a Python Pandas program to convert a Numpy array to a Pandas series

import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
pd_srs = pd.Series(arr)
print(pd_srs)