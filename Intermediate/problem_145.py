# Problem 145
# Write a Python Numpy program to create an array, store in a text file and
# display the result.

import numpy as np
two_array = np.array([5, 4, 0, 2, 0])

with open(file='problem_1454.txt', mode='w+') as file:
    content = str(two_array)
    file.write(content)
    file.close()

