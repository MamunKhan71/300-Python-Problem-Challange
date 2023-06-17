# Problem 18
# Write A Python Program to store name, address, contact in dictionary, and then update his/her contact number

new_dict = {
    "name": "Mamun",
    "address": "Dhaka",
    "contact": "01643091606",
}

new_dict['name'] = "Khan"  # First Method
new_dict.update({"contact": "01643060716"})  # Second Method
print(new_dict.values())
