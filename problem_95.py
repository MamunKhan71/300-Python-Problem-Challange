# Problem 95
# Write Python Program To Get Number From User To Display Table In
# Reverse Order
# Example:
# 2* 10 = 20
# 2 * 09 -18
# And so on

inpt = int(input('Number: '))

for num in range(10, 0, -1):
    print(f"{inpt} X {num} = {inpt*num}")