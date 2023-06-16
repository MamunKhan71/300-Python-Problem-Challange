# Problem 59
# Write A Python Program To Make A Decimal To Binary Conversion Calculator
from math import floor
reminder = []
inpt = int(10)
while inpt/2 != 0:
    reminder.append(str(inpt % 2))
    inpt = int(floor(inpt/2))

print(''.join(reversed(reminder)))