# Problem 98
# Write A Python Program To Find Square Root Of Middle
# Element Of List Items

import math

lst = [1, 2, 3, 54, 5, 6, 7, 98, 95, 5, 6, 7, 8, 99]
print(math.sqrt(lst[math.ceil(len(lst)/2)]))