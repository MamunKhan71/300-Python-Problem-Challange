# Problem 66_1
# Program to display prime numbers from a given number
flag = 0
user_input = int(input("Enter Your Number: "))
for nm in range(1, user_input + 1):
    if user_input % nm == 0:
        flag += 1

if user_input == 1:
    print("Neither Prime or Neither Composite")
elif flag > 2:
    print("Not a prime Number")
else:
    print("Prime Number")
