# Problem 135
# Write a Python Numpy Program to Create a array of zero. According to user entered number.
import numpy as np
from numpy import empty

userInput = input("Enter array size (row x column): ").split('x')
arr = np.full((int(userInput[0]), int(userInput[1])), 0, dtype=int)
print(arr)