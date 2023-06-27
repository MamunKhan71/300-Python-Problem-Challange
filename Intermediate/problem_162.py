# Problem 162
# Write a Python program to convert array float data type to integer data type.

import numpy as np

arr = np.array([1, 2, 3, 4], dtype=float)
arr_cnvrt = arr.astype(int)
print(arr_cnvrt)
