# Problem 76
# Write A Python Program Which Display Numbers That Are Divisible By 3, 5 From A List

lst = [1, 2, 4, 54, 6, 7, 88, 64, 67, 84, 35]
for num in lst:
    if num % 3 == 0 or num % 5 == 0:
        print(num)
    else:
        continue
