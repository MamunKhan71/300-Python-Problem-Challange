# Problem 34
# Write A Python Program To Get 5 Color name From The User In List,
# Display That List, Remove Las Color And Then Display All The Colors to User

colors = [input("Enter Color Name : ") for _ in range(5)]
print(f"Before Removing the last: {colors}")
colors.pop()
print(f"After Removing the last: {colors}")

