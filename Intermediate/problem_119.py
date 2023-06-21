# Problem_119
# Write a Python Program To Get a word from user. The word should
# contain lower and uppercase both. Then convert lower to upper and
# upper to lower

inpt = list(input("Enter the string: "))
for index, value in enumerate(inpt):
    if value.isupper():
        inpt[index] = inpt[index].lower()
    else:
        inpt[index] = inpt[index].upper()
print(''.join(inpt))
