# Problem 45
# Write A Python Program To Display Number From 1 To 30, Only Odd Number
for nm in range(1, 31):
    print(nm) if nm % 2 != 0 else print('', end='')
