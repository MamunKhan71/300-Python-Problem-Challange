# Problem 67
# Write A Python Program To Find Sum Of Two Number (That Number Should Be Positive And Less Than 50)
while True:
    number = int(input("Enter Number 1: "))
    number2 = int(input("Enter Number 2: "))
    if 0 <= number < 50 and 0 <= number2 < 50:
        print(f"Sum is: {number+number2}")
        break
    else:
        print("Please insert number between 0 to 50")
