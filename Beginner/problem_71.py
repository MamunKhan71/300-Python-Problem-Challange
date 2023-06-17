# Problem 71
# Write a python program to count a specific word or characters in a sentence

count = int(0)
letter_search = input("Enter the letter you want to search: ")
if len(letter_search) > 1:
    user_input = input("Please Enter Your Sentence: ").split(' ')
else:
    user_input = list(input("Please Enter Your Sentence: "))
for char in user_input:
    if char == letter_search or char == letter_search.upper():
        count += 1
print(f"The {'letter' if len(letter_search) == 1 else 'word'} '{letter_search}' occurred {count} times in this sentence!")
