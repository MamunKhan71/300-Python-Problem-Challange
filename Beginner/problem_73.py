# Problem 73
"""
Write A Python Program To Get A Sentence From User, To Display Last Character Of That Sentence AND Also Display All The
Characters One By One
"""
inpt = input("Enter The Sentence: ")
print(f"Last Character: {inpt[-1]}\nAll Character :")
for i in inpt:
    print(i)