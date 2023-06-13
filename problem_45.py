# Problem 45
# Write A Python Program To Display Number From 1 To 30, Only Odd Number
print("Even\t\tOdd")
counter = int(0)
for nm in range(0, 32):
    counter += 1
    print(f"{nm}\t\t\t", end='') if nm % 2 == 0 else print(f'{nm}', end='')
    if counter == 2:
        print("\n")
        counter = 0