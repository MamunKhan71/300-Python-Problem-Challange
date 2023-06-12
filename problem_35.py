# Problem 35
# Python Program To Get 10 Name Of The Students From The User In A List, Display That Students Name In descending Order

# Starts Here

user_name = [input(f"Enter Your Name {_}: ") for _ in range(1, 11)]
print(sorted(user_name, reverse=True))

# Removing the first and last element and after sorting in descending order
# user_name.pop(0)
# user_name.pop()
# print(sorted(user_name, reverse=True))

