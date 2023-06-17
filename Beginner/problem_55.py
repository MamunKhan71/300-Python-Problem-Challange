# Problem 55
# Write A Python Program To Show The Current Date On The User Request
from datetime import date,datetime
confirm = input("Do you want to get the date and time?(Y/N): ")
if confirm == "Y":
    print("Today's Date: " + str((date.today()).strftime("%d %B %Y")))
    print("Time Now: " + str((datetime.now().time()).strftime("%H Hour %M Minutes and %S Seconds")))
else:
    print("You pressed N")