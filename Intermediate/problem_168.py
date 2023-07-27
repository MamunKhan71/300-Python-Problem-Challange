# Problem 168
# Write a Python Program to perform different operation on excel file

import pandas as pd

data = pd.read_excel("xls.xlsx")
# Sum of the selected column
print(f"Sum : {data['Orders'].sum()}")
# Product of the selected column
print(f"Product : {data['Orders'].prod()}")
# Count of the selected column
print(f"Total Value : {data['Orders'].count()}")