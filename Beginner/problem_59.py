# Problem 59
# Write A Python Program To Get A Bio From A User And Count Number Of Character And Word In Bio Description

user_input = input("Write your bio: ")
total_character = len(user_input)
total_word = len(user_input.split(" "))
print(f"Total Word: {total_word}\nTotal Character: {total_character}")