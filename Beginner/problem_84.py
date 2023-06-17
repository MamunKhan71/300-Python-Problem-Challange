# Problem 84
# Write A Python Program To Get Name From User, To Check It Is In Uppercase Or Not,
# If Not Upper Then Convert Into Uppercase

name = input('Enter Your Name: ')
if name.isupper():
    print(name)
else:
    print(name.upper())