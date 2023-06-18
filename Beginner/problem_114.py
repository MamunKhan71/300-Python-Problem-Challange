# Problem 114
# Write a Python program to find most occurring element in a given list of numbers
from pprint import pprint

from collections import Counter

numList = [1, 2, 43, 5, 6, 7, 8, 2, 5, 43, 43, 43, 43, 43, 3, 52, 2, 57, 2, 6, 72, 2]
frequency_list = Counter(numList)
most_common = frequency_list.most_common(1)

maxFreq = most_common[0][0]
maxFreqCount = most_common[0][1]

print(f"Most frequent element: {maxFreq}")
print(f"Frequency: {maxFreqCount}")