# Problem 39
# Write A Python Program To Get 5 Number In The List, Pass That List In The
# Function To Multiply And Add That Number And Display Total Result

# # For Multiplication
def Multiplier(num_lst):
    mulList = int(1)
    for num in num_list:
        mulList *= num
    return mulList

# For Addition
def Adder(num_lst):
    addList = int(0)
    for num in num_list:
        addList += num
    return addList


num_list = [int(input(f"Enter Number {_} : ")) for _ in range(1, 6)]
print(f"Multiplication : {Multiplier(num_list)}")
print(f"Addition : {Adder(num_list)}")

