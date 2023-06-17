# Problem 45
# Write A Python Program To Display Number From 1 To 30, Only Odd Number
print("Even\t\tOdd")
for nm in range(0, 32):
    print(f"{nm}\t\t\t", end='') if nm % 2 == 0 else print(f'{nm}')