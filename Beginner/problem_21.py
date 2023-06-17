# Problem 21
# a Write a Python Program to get 5 number from user in array, find the maximum number
from array import array
numList = array('i', [int(input("Enter Your Number: ")) for _ in range(5)])
print(max(numList))