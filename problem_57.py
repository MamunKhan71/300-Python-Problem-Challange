# Problem 57
# Write A Python Program To Make Average Calculator
user_input = list(map(int, input("Enter all the marks one by one separated by space: ").split(" ")))
print(f"Average : {sum(user_input)/len(user_input)}")