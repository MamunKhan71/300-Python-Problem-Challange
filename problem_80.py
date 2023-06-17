# Problem 80
# Write A Python Program To Print Characters From A String That Are Present At An Odd Index Number

inpt = input('Enter Your String: ')
print("Odd Index are: ", end='')
for index, value in enumerate(inpt):
    if index % 2 != 0:
        print(value+" ", end='')
    else:
        continue
