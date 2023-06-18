# Problem 107
# Write A Python Program To Store Students Records, User Will Be Able To Delete Any Student From A Record On Run Time
def studentList(studentListss):
    for index, value in enumerate(studentListss):
        print(f"{index + 1}. {value}")


studentLists = [input("Student Name: ") for _ in range(5)]
studentList(studentLists)
user_remover = (int(input("Please enter the student no to remove: "))-1)
studentLists.pop(user_remover)
print("Successfully Removed\nUpdated List: ")
studentList(studentLists)

