# Problem 96
# Python Program To Get 10 Data Item From User, How Much Integer, Float And String Type Of Data Is Stored In A List

lst = [1, 2, 'Mamun', 9.5, 'khan', 22, 8.77]
strCounter = int(0)
intCounter = int(0)
floatCounter = int(0)
for num in lst:
    if type(num) == str:
        strCounter += 1
    elif type(num) == int:
        intCounter += 1
    elif type(num) == float:
        floatCounter += 1
print(f"Total int: {intCounter}\nTotal Float: {floatCounter}\nTotal String: {strCounter}")