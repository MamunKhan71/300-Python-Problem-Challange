# Write A Python Program To Convert Radian To Degree
# Starts Here:
import math

number = float(input("Enter Your Number in Radian: "))
degree = float("{:.3f}".format(number * 180 / math.pi))
print(f"Number in degree is : {degree}")

# Degree to Radian
# number = float(input("Enter Your Number in Degree: "))
# rad = float("{:.3f}".format(number * math.pi/180))
# print(f"Number in radian is : {rad}")
