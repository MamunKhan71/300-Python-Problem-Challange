# Problem 43
"""
Write A Python Program To Get Starting Number And Ending Number
From The User To Display That Number With Proper Sequence
As, User Input 5 As Starting Number And IO As A Ending Number, Then It
Should Display
5, 6, 7, 8, 9,10
"""
starting = int(input("Enter The Starting Number: "))
ending = int(input("Enter The Ending Number: "))
for _ in range(starting, ending+1):
    print(f"{starting}")
    starting += 1