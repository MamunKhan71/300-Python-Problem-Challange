# Problem 172
# Write a Python program to read a CSV file as a list

import csv
ex_ls = []
with open(file='problem70.csv', mode='r') as file:
    ebk = csv.reader(file)
    for i in ebk:
        ex_ls.append(i)

print(ex_ls)