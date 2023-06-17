# Problem 60
# Write A Python Program To Get 5 Author Name With Their Book Name And Display Last Author With It's Book Name
book_details = {}
i = 2
while i != 0:
    book_name = input('Book Name : ')
    book_author = input('Book Author: ')
    book_details[book_name] = book_author
    i -= 1

print(f"Last Book : {list(book_details.keys())[-1]}")
print(f"Author Name : {list(book_details.values())[-1]}")