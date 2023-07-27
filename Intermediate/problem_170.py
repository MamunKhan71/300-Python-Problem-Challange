# Problem 170
# Write a Python Program to Display positive and negative in a list. When there is Positive and Negative number.

num_list = [1, 2, -3, 4, -5]
n_list = []
new_list = [n_list.append("Negative") if x < 0 else n_list.append("Positive") for x in num_list]
print(n_list)