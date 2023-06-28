# Problem 163
# Write a Python Program to Create an Excel file using python using xlswriter library

import xlsxwriter as xw
workbook = xw.Workbook(filename='problem_163.xlsx')
work_sheet = workbook.add_worksheet()
work_sheet.write('A1', 'Mamun')
work_sheet.write('B1', 'Mahtab')
work_sheet.write('C1', 'Minha')
workbook.close()

