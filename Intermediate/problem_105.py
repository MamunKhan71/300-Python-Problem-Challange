# Problem 105
# Write A Python Program To Calculate Circumference And Area Of A Circle
# We know Circumference C = 2πr
# We know area a = 2πr^2
import math

radius = float(input("Enter the radius: "))
c = round(2*math.pi*radius, 2)
a = round(2*math.pi*pow(radius, 2), 2)
print(f"Circumference: {c}\nArea: {a}")
