# Problem 120
# Write a Python program to count total number of lists in a nested list.
from itertools import count

lst = [['Apple', 'Banana', ['Mango', 'Pineapple']], ['Beef', 'Mutton', 'Chicken'], ['Lacchi', 'Juice', 'Coca-Cola'], ['Lemon', 'Salad', ['Tomato', 'Catchup']]]
lst_total = int(0)
for i in lst:
    print(i)
    if type(i) == list:
        lst_total += 1
print(lst_total)