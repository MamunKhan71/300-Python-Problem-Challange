# Problem 10
# Write A Python Program To Get Number From The User, And Display Table For That Number.

number = int(input("Number : "))
print("You entered " + str(number))
print("--------------")
for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")
