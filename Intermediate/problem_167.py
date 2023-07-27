# Problem 167
# Write a Python Program to read specific column data from excel.
import pandas as pd

col = [0, 1, 2]
xcl = pd.read_excel("xls.xlsx", usecols=col)
print(xcl)
