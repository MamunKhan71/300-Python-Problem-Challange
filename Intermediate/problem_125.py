# Problem 125
# Write a Python program to print a dictionary items line by line. Key and
# value should have one tab distance.

color = {
    1: "Red",
    2: "Blue",
    3: "Green",
    4: "Yellow",
}

for key, value in color.items():
    print(f"{key}\t{value}")
