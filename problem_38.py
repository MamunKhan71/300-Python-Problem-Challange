# Write A Python Program To Convert Radian To Degree
# Starts Here:
import math
number = float(input("Enter Your Number in Radian: "))
degree = float("{:.3f}".format(number * 180/math.pi))
print(f"Number in degree is : {degree}")