# Problem 140
# Write a NumPy program to create one-dimensional array, getting number
# element from user using for loop.
import numpy as np
array_dimension = int(input("One-Dimension: "))
new_array = np.zeros(array_dimension, dtype=int)
for i, v in enumerate(new_array):
    new_array[i] = int(input("Number: "))

print(new_array)