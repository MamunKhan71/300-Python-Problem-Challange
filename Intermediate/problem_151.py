# Problem 151
# Write a Python Program to Create a list from existed list that contain
# uppercase words

old_list = ['Mamun', 'limon', 'Rayhan', 'RAJON', 'FAISAL', 'sopnil']
new_list = [x for x in old_list if x.isupper()]
print(new_list)