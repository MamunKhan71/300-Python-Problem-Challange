# Problem 171
# Write a Python Program to count number of instances of a Python class.
class Instance:
    x = int(0)

    def __init__(self):
        Instance.x += 1


new = Instance()
new2 = Instance()
new3 = Instance()
new4 = Instance()
print(new.x)
