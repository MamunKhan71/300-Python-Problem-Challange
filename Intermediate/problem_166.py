# Problem 166
# Write a Python program to insert an element before each element of a list.

demo_list = ['1', '2', '3', '4']
user_input = input('Enter the prefix : ')
for i, v in enumerate(demo_list):
    demo_list[i] = f"{user_input}{i}"

print(demo_list)

