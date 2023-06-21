# Problem 126
# Write a Python program to filter odd numbers from a given dictionary
# keys. Display only those values which have odd keys.

color = {
    1: "Red",
    2: "Blue",
    3: "Green",
    4: "Yellow",
    5: "Orange",
    6: "Magenta",
    7: "Cyan",
    8: "Black",
    9: "Purple",
    10: "Gray",
}

for key, value in color.items():
    if key % 2 != 0:
        print(value)
    else:
        continue
