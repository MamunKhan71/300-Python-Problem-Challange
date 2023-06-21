# Problem 123
# Write a Python program to get 5 number from user to store in a list.
# Display all the numbers with power of 3 using list comprehension.

print([pow(int(input(f"Number {_}: ")), 3) for _ in range(5)])
