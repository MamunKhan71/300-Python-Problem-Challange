# Problem 146
# Write a Python Numpy program to create a 4x4 zero matrix with elements
# on the main diagonal equal to 6, 7, 8, 9.

import numpy as np

diag_array = np.zeros(shape=(4, 4), dtype=int)
np.fill_diagonal(diag_array, (6, 7, 8, 9))
print(diag_array)
