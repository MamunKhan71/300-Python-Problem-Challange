# Problem 57
# Write A Python Program To Make Average Calculator
user_input = list(map(int, input("Enter all the marks one by one separated by space: ").split(" ")))
total_marks = sum(user_input)
print(f"Average : {total_marks/len(user_input)}")