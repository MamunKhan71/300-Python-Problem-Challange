# Problem 128
# Write a Python program to convert dictionary's keys and values into two
# list. One list should store keys and other list should store values.

keyList = []
valueList = []

color = {
    '1': "Red",
    '2': "Blue",
    '3': "Green",
    '4': "Yellow",
    '5': "Orange",
    '6': "Magenta",
    '7': "Cyan",
    '8': "Black",
    '9': "Purple",
    '10': "Gray",
}

for key, value in color.items():
    keyList.append(key)
    valueList.append(value)

print(f"Keys : {keyList}")
print(f"Values : {valueList}")
