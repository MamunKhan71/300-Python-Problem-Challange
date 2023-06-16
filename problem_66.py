# Problem 66
# Write A Python Program To Create A List To Pass To Function As Parameter To Display Its Element In Reverse Order

def Reverser(data):
    reverList = []
    for _ in data[::-1]:
        reverList.append(_)
    return reverList


print("Fruit Name")
fruit = [input("Name: ") for _ in range(5)]
rLists = Reverser(fruit)
print(rLists)
