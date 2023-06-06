# Problem 12
# Write a Python program to display following output using for loop
"""
*
* *
* * *
* * * *
* * * * *
"""
for num in range(0, 6):
    for n2 in range(0, num):
        print("* ", end='')
    print("")