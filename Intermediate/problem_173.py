# Problem 173
# Write a Python program to multiply with every number with user entered number in a list

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = int(input("Enter the number you want to multiply: "))
num_list = [(x * user_input) for x in num_list]
print(num_list)
