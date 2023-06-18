# Problem 108
# Write a Python Program To Update Specific Key In A Dictionary

my_dict = {
    "Name": "Mamun",
    "Age": 20,
    "Email": "mkmamun031@gmail.com",
    "Address": "Dhaka",
    "Phone": "01643091606",
}
userInput = input("Enter the key you want to update: ")
newKey = input("Enter the name of the new key: ")
my_dict[newKey] = my_dict[userInput]
del my_dict[userInput]
print(my_dict.get('Mobile'))