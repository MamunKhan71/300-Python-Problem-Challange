# Problem 56
# Write A Python Program To Make A Percentage Calculator
amount = int(input("Enter the amount: "))
percentage = int(input("Enter the percentage: "))
discount = ((amount*percentage)/100)
print(f"Discounted Amount: {discount}")
print(f"Price After Discount: {amount-discount}")