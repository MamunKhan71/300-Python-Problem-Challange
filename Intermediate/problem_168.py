# Problem 168
# Write a Python Program to perform different operation on excel file

import pandas as pd

data = pd.read_excel("xls.xlsx")
# Sum of the selected column
print(data['Orders'].sum())
# Product of the selected column
print(data['Orders'].prod())