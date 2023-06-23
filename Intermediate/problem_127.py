# Problem 127
# Write a Python program to get the total length of all keys of a dictionary
# with string keys.


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
key_length = int(0)
for i in color.keys():
    key_length += len(i)
print(key_length)