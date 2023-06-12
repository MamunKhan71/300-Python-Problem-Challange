# Problem 41
# Write A Python Program To Get a Angle From The User And Find Its Sin And Cos Value In Radian
import math

angle = float(input("Enter the angle: "))
sin_value = "{:.3f}".format(float(math.sin(angle)))
cos_value = "{:.3f}".format(float(math.cos(angle)))

print(f"Sin Value: {sin_value}\nCos Value: {cos_value}")
# In Degree
print(f"Sin Value in deg: {float(sin_value)*180/math.pi}\nCos Value in deg: {float(cos_value)*180/math.pi}")
