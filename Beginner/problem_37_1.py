# Problem 37_1
# Write A Python Program To Get 6 Number From The User To Find
# The Square Of First Three Number And Find Cube Of Next Three Number
lst = [int(input(f"Enter num {_} : ")) for _ in range(1, 7)]
for num in lst:
    print(f"Cube : {pow(num, 3)}") if num >= 4 else print(f"Square: {pow(num, 2)}")