# Problem 32
"""
Write A Python Program To Get Two Number From The User , Pass To Function And Find Maximum
"""
from itertools import chain


def maximum(num1, num2):
    # To find the minimum, simply just place < sign in place of > sign
    if num1 > num2:
        return num1
    else:
        return num2


max = maximum(input("Enter First Number: "), input("Enter Second Number: "))
print(max)
