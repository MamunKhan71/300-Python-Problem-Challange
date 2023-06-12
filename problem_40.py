# Problem 40
"""
Write Python Program To Get A Username From The User That Should Have Alphanumeric Characters,
Then Pass That Username To Function As Parameter, To Display That Username
"""


def AlphaNumeric(name):
    if name.isalnum():
        print(name)
    else:
        print("No Alphanumeric Character Found!")


userInput = input("Enter Your Username : ")
AlphaNumeric(userInput)
