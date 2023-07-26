# Problem 119
# Write a Python Program To Get a word from user. The word should
# contain lower and uppercase both. Then convert lower to upper and
# upper to lower.

userInput = list(input("Enter Your Word: "))
for i, v in enumerate(userInput):
    if v.isupper():
        i = v.lower()
    else:
        i = v.upper()
print(''.join(userInput))