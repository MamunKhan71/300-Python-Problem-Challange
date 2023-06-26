# Problem 152
# Write a Python Program to Create set that display only even number

set_A = set()
while True:
    inpt = input("Enter Your Number: ")
    if inpt == 's':
        break
    elif int(inpt) % 2 == 0:
        set_A.add(int(inpt))
    else:
        continue
print(set_A)
