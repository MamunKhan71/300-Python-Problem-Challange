# Problem 57
# Binary to decimal converter
binary = list(input("Enter the number: "))
length = len(binary)
sums = int(0)
for index, value in enumerate(binary[::-1]):
    sums += int(value)*pow(2, index)
print(sums)
