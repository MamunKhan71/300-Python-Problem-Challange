# Problem 48
# Swap two numbers

num1 = int(input("Enter A: "))
num2 = int(input("Enter B: "))
print("Before Swapping ")
print(f"Num A : {num1}\tNum B: {num2}")
print("After Swapping ")
temp = num1
num1 = num2
num2 = temp
print(f"Num A : {num1}\tNum B: {num2}")

