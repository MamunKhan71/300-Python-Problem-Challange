# Problem 138
# Write a Python NumPy program to make an array of equal shape having same data type of a given array.
import numpy as np

given_array = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 5]])
array_shape = given_array.shape
new_array = np.zeros(shape=array_shape, dtype=object)
print(new_array)

# Alternative
# Write a Python NumPy program to make an array of equal shape having same data type of a given array.
# import numpy as np
#
# given_array = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 5]])
# new_array = np.zeros_like(given_array)
# print(new_array)
