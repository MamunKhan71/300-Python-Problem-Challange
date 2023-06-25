# Problem 136
# Write a Python OOP program to get a number from user to display its table

class multiplicationTable:
    def __init__(self, number):
        self.number = number

    def getTable(self):
        for i in range(1, 10+1):
            print(f"{self.number} X {i} = {self.number*i}")


mTbl = multiplicationTable(int(input("Number: ")))
mTbl.getTable()