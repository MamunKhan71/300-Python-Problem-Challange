# Problem 150
# Write a Python Program to Create list from existed list that count number
# less than 20 greater than 5

old_list = [1, 2, 5, 6, 10, 50, 20, 30, 19, 7, 12, 40, 18, 4, 16, 3, 15, 15, 14]
new_list = [x for x in old_list if 5 < x < 20]
print(new_list)
