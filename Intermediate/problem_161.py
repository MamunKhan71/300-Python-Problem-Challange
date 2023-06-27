# Problem 161
# Write a Python Program to display only those number that are divisible by
# 4 or 5 from list, using list comprehension.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = [x for x in lst if x % 4 == 0 or x % 5 == 0]
print(new_list)
