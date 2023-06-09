# Problem 16
# Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display
userList = [int(input("Enter Your Number: ")) for _ in range(6)]
print(f"Before Removing : {userList}")
print(f"After Removing : {userList.clear()}")

