# Problem 70
# Write A Python Program To Check Duplication of Student Identity In Student List and remove it

inpt = []
unique_id = []
while True:
    inptS = input("Student ID: ")
    if inptS == 's':
        break
    else:
        inpt.append(inptS)
for student_id in inpt:
    if student_id not in unique_id:
        unique_id.append(student_id)
print(unique_id)