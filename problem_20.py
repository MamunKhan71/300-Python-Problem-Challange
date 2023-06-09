# Problem 20
# Write A Python Program To Get 5 Number From User In Array And Sum All Number And Display
from array import array
numArray = array('i', [int(input("Enter Your Number: ")) for _ in range(5)])
print(sum(numArray))