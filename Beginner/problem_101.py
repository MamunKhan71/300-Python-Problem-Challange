# Problem 101
# Write A Python Program To Display All The Student Name Except With Start 'f' Char

name = ["Mamun", "Nahid", "Zarin", "Soha", "Fuad", "Farhan", "Limon"]

for nm in name:
    if nm[0].upper() != "F":
        print(nm)
    else:
        continue