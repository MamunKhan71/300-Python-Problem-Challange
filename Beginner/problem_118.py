# Problem 118
# Write a Python program to count any item from a nested list
number_list = [[1, 2, 2, 4, 5], [1, 2, 3, 4, 6, 8]]
search_value = int(input("Search: "))
result = sum(i.count(search_value) for i in number_list)
print(f"The value {search_value} appeared {result} times!")