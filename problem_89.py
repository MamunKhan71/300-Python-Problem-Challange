# Problem 89
# Write A Python Program To Generate Number From 0 To 20 Only Even Number And
# Generate 0 To 20 Odd Number. Add Both Generated Number To Each Other To Display
# Total Result
even = int(0)
odd = int(0)
for i in range(0, 20):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("Sum of even and odd : " + str(even+odd))
