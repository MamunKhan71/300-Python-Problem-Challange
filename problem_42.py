# Problem 42
# Write A Python Program To Generate 1 To 10 Number With Their Square
# And Cube And Also Display Their Addition (Square + Cube)
print("Number\tSquare\tCube\tAddition")
for nm in range(1, 11):
    print(f"{nm}\t\t{pow(nm,2)}\t\t{pow(nm,3)}\t\t{pow(nm,2)+pow(nm,3)}")
