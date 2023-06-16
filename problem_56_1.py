# Problem 59
# Write A Python Program To Make A Decimal To Binary Conversion Calculator
from math import floor
inpt = int(input("Enter the decimal number: "))
binary = ""
while inpt/2 > 0:
    binary = str(inpt % 2) + binary
    inpt //= 2
print(f"Binary : {binary}")
