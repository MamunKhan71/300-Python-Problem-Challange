# Problem 155
# Write a Python Numpy Program to replace any number in Array

import numpy as np

array = np.array([1,2,3,4,5])
print(f"Array: {array}")
numberReplacer = int(input("Enter the number you want to replace: "))

for i,v in enumerate(array):
    if v == numberReplacer:
        array[i] = int(input("New Number: "))
    else:
        continue

print(array)
