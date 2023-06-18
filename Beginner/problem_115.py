# Problem 115
# Write a Python program to create a parameterized and non parameterized constructor
class MyClass:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def adder(self):
        return self.x + self.y


newCon = MyClass(x=5, y=10)
print(newCon.adder())