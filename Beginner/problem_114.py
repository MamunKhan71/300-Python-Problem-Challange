# Problem 114
# Write a Python program to find most occurring element in a given list of numbers
from pprint import pprint

numList = [1, 2, 43, 5, 6, 7, 8, 2, 5, 43, 43, 43, 43, 43, 43, 3, 52, 2, 57, 2, 6, 72, 2]
frequency_list = {}
maxFreq = None
for i in numList:
    if i in frequency_list:
        frequency_list[i] += 1
    else:
        frequency_list[i] = 1
des_value = max(frequency_list.values())

for key, value in frequency_list.items():
    if value == des_value:
        maxFreq = key
        break
print(f"Maximum Frequent Element: {maxFreq}")