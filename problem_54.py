# Problem 54
# Write A Python Program To Get A Number From The User To Find Factorial Of That Number
import math

factorial = int(1)
inp = int(input("Enter a number to find its factorial: "))
if inp >=1:
    for num in range(1, inp + 1):
        factorial *= num
else:
    print("Please Insert a valid value..")
print(factorial)
# <!--- Another Method ---!>
# Using math.factorial library function
print(math.factorial(inp))