# Problem 157
# Write a Python Program to append array element to existing array

import numpy as np
from array import *

x = array('i', [1, 2, 3, 4, 5])
print(f"Before Appending: {array}")
x.append(22)
for itm in x:
    print(str(itm) + ' ', end='')