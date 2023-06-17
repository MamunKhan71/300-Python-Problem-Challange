# Problem 90
# Write A Python Program To Get Age Of 10 Students From User And Store
# In A List. Condition Is That, System Should Display Age That Greater Than
# 14 Year And Less Than 20 Year

age = [int(input("Age: ")) for _ in range(10)]

for i in age:
    if 14 <= i <= 20:
        print(i)
    else:
        continue
