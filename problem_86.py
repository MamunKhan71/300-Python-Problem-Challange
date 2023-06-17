# Problem 86
# Write A Python Program To Search Any Character (or Set of Character From a String)
user_input = list(input("Enter Your Sentence: ").upper().split(' '))
user_chars = input("Search: ").upper()
for name in user_input:
    if name in user_chars:
        print("Yes")
    else:
        continue
