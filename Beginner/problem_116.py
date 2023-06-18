# Problem 116
# Write a Python program to create a class of student having two data
# member (name and id) having a two methods, one is used to get name
# and id and other is to display name and id to user.
class StudentInfo:
    def __init__(self):
        self.name = None
        self.ids = None

    def get_info(self, name, ids):
        self.name = name
        self.ids = ids

    def display_info(self):
        print(self.name)
        print(self.ids)


stInfo = StudentInfo()
stInfo.get_info("Mamun", "54")
stInfo.display_info()
