# Problem 169
# Write a Python Program to find maximum and minimum number from a excel file
import pandas as pd

data = pd.read_excel("xls.xlsx")
print(f"Maximum Number: {data['Orders'].max()}")
print(f"Minimum Number: {data['Orders'].min()}")