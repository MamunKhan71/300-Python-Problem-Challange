# Problem 134
# Write a Python Numpy program to check element whether it is NaN or not.
import numpy as np
noneCheck = np.array([1, 2, np.nan, 4])
print(np.isnan(noneCheck))
