# Problem 133
# Write a Python Program to Create a dictionary which display those value
# which have vowel character.
import re
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
    '10': "STC",
}
for i in color.items():
    if re.search('a|e|i|o|u|A|E|I|O|U', i[1]):
        print(f"Found Vowel in : {i[1]}")