# Problem 82
# Write a Python Program To Append Those Number That Are Divisible By And 7 From a Range (10, 100) To A New Created List
newList = [x for x in range(10, 100) if x % 5 == 0 or x % 7 == 0]
print(newList)
