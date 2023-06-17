# Problem 83
# Write A Python Program To Get Name From A List, That Start From 'f'
lst = ['Mamun', 'Fahim', 'Jahid', 'Julash', 'Forhad', 'Symon', 'Habib', 'Promi', 'Fuad']
for name in lst:
    if name[0].upper() == 'F':
        print(name)
    else:
        continue

