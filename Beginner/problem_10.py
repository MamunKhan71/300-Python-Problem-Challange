# Problem 10
# Write A Python Program to get 6 subject marks from the user and calculate total and average of that
# marks. And display to user.
numbers = []
for num in range(0, 6):
    numbers.append(float(input(f"Enter Subject {num+1} : ")))

print(f"Average Mark Is : {sum(numbers)/len(numbers)}")
