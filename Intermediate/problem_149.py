# Problem 149
# Write a Python Program to Create a dictionary from list that display its
# square as value.
import math

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_dict = {x: int(math.pow(x, 2)) for x in new_list}
print(new_dict)
