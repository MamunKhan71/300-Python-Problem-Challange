# Problem 148
# Write a Python Program Create dictionary from existed dictionary which
# display length of words as value

old_dict = {
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
new_dict = {key: len(value) for key, value in old_dict.items()}
print(new_dict)

##
# Alternative Way
# ##
# for index, value in old_dict.items():
#     new_dict[index] = len(value)
# print(new_dict)
