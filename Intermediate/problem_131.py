# Problem 131
# Write a Python Program to update any value in a dictionary on user request.


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
print(color)
print("-----------")
userInput = input("Which key you want to update? : ")
color[userInput] = input("New Value: ")
print(color)