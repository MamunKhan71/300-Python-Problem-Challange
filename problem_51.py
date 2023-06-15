# Problem 51
# Write Python Program To Find Number Of Day Between Two Dates
from datetime import datetime
dt = input("Enter the starting date (DD-MM-YY : ")
dt2 = input("Enter the ending date (DD-MM-YY : ")
newDate1 = datetime.strptime(dt, '%d-%m-%y')
newDate2 = datetime.strptime(dt2, '%d-%m-%y')
print(f"Total Days: {(newDate2-newDate1).days}")