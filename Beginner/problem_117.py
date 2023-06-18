# Problem 117
# Write a Python program to get a number from user to display square of its previous number and next number
number = int(input("Number: "))
print(f"Square of previous number: {pow(number-1, 2)}\nSquare of next number: {pow(number+1, 2)}")