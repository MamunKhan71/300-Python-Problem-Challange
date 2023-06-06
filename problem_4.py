# Problem 4
# Program to check whether a person is eligible for voting or not

age = int(input("Enter Your Age : "))

if age >= 18:
    print("Eligible for voting")
else:
    print(f"Sorry! You can not participate in voting, you will be able to participate after {18-age} year!")