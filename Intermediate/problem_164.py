# Problem 163
# Write a Python program to read an excel file using xlwings

import xlwings as xw

dta = xw.Book(fullname='problem_163')
sheet = dta.sheets('Sheet1')
sheet['A1'].value = 'Mamun'
sheet['A2'].value = 'Minha'
sheet['A3'].value = 'Mahtab'

