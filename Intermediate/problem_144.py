# Problem 144
# Write a Python Numpy program to convert array element to Boolean value
import numpy as np
two_array = np.array([5, 4, 0, 2, 0])

bool_array = two_array.astype(bool)
print(bool_array)