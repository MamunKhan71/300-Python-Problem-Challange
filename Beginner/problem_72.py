# Problem 72
# Write A Python Program To Shuffle a List Of Different Color Code
import random
color_code = [input("Enter Color Code: ") for _ in range(5)]
random.shuffle(color_code)
print(color_code)