# Problem 165
# Write a Python Program to write data to excel cell using python xlsx-write
import xlsxwriter
wb = xlsxwriter.Workbook('xls.xlsx')
worksheet = wb.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('A2', 'Phone')
worksheet.write('B1', 'Mamun')
worksheet.write('B2', '01643091606')
wb.close()

