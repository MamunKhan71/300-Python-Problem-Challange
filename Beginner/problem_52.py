# Problem 52
# Write A Python Program To Get A Sentence From The User, To Reverse That Sentence
newChar = ""
user_input = input("Enter a sentence: ")
rev_input = reversed(list(user_input))
print(''.join(rev_input))