# Problem 69
# Write A Python Program To Create A File And Write User Name, And Age In That File
name = input("You Name: ")
age = input("You age: ")
with open(file="problem_69_output.txt", mode='w') as file:
    file.write(f"Name: {name}\nAge: {age}yrs!")
    file.close()