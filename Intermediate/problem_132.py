# Problem 132
# Write a Python Program to Create a Dictionary to find addition of all the
# keys and Product of all the values from a dictionary.

color = {
    1: 100,
    2: 200,
    3: 300,
    4: 400,
    5: 500,
}
keys = int(0)
values = int(1)
for key, value in color.items():
    keys += int(key)
    values *= int(value)
print(keys)
print(values)