# Problem 122
# Write a Python program to access multiple elements from a list.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = int(input("Enter Starting Point: "))
end = int(input("Enter Ending Point: "))
for i in lst[start:end]:
    print(i)