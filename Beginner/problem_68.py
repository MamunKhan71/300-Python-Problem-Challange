# Problem 68
# Write A Python Program That Accepts Six Identity Numbers Of Students As Input And Display In Descending Order

numbers = [int(input(f"Number {_+1}: ")) for _ in range(0, 6)]
desNum = []
for i in range(0, 6):
    for j in range(i, 6):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)

