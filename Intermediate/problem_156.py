# Problem 156
# Write a Numpy program to perform addition, subtraction, division and
# multiplication on Array Element.

import numpy as np

array = np.array([1, 2, 3, 4, 5])
inpt_sign = input("Enter the sign: ")
inpt_num = input("Enter the num: ")

for index, value in enumerate(array):
    array[index] = eval(f'{value}{inpt_sign}{inpt_num}')

print(array)