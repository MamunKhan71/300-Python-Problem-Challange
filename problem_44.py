# Problem 44
"""
Write A Python Program To Get Large Number As Starting And Lower Number As
Ending Number, Display That Number From Large To Lower.
As User Input 10 As Large Number And 5 As Lower Number, Then It Should Display As:
10,9,8,7,6,5,4,3,2,1..
"""
starting = int(input("Starting : "))
ending = int(input("Ending : "))
for num in range(starting, ending-1, -1):
    print(num)
