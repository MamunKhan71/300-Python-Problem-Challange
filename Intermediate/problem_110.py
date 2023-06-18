# Problem 110
# Write a Python Program to reverse a sub string from a string
inpt = input("Enter the string: ")
start = int(input("Starting index: "))
end = int(input("Ending index: "))
reverse = reversed(inpt[start:end])
print(''.join(reverse))