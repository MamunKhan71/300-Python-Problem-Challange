# Problem 147
# Write Python Program to make use of isidentifier method with string

user_input = input("Enter the identifier: ")
if user_input.isidentifier():
    print("Valid Identifier")
else:
    print("Invalid Identifier!")
