# Problem 141
# Write a Numpy Program To Create a Two-dimensional Array & Multiply
# with any number to that array elements. That number take from user.
import numpy as np

two_array = np.array([[5, 4, 3, 2, 1],
                      [9, 8, 7, 6, 5]])
inpt = int(input("Insert Any Number : "))

for i,v in enumerate(two_array):
    two_array[i] *= inpt

print(two_array)
