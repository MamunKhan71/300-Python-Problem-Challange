# Problem 11
# Write A Python Program To Get 2 Number From The User And Display Maximum Number

num1, num2 = map(int, input("Enter The Numbers separated by comma: ").split())
print(f"Max Num is : {max(int(num1), int(num2))}")
