# Problem 158
# Write a Python Program to Display element of list with their occurrence

lst = [1, 2, 4, 6, 7, 8, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 4, 2, 1, 4, 6, 9, 9]
un_lst = list(set(lst))
for i in un_lst:
    count = lst.count(i)
    print(f"{i} appeared {count} times!")
