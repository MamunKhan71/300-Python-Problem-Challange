# Problem 100
# Write A Python Program To Add Number From List That Are Greater Than 5 And Less Than 10
lst = [1, 5, 10, 50, 20, 9, 7, 8]
for nm in lst:
    if 5 < nm < 10:
        print(nm)
    else:
        continue
