# Problem 85
# Write A Python Program To Get Name From A List, That Ends At 'n'
name_list = ['banana', 'orange', 'Lemon', 'jackfruit', 'Clemon']

for name in name_list:
    if name[-1] == 'n':
        print(name)
    else:
        continue
