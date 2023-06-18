# Problem 113
# Write A Python Program To Get a length in mm and convert to m and km

mmLength = float(input("Enter the length(mm): "))
meter = mmLength/1000
km = mmLength / 1000000
print(f"Meter: {meter}\nKilometer: {km}")