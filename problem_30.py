# Problem 30
# Write A Python Program To Get A Number From User To Check, It Is Divisible By 2 And 3

print("Divisible" if (number := int(input("Enter Any Number: "))) % 2 == 0 or number % 3 == 0 else "Not Divisible")