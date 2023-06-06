# Problem 13
# Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic
passInput = input("Enter Your Password: ")

if passInput.isalnum():
    print("Your password is valid")
else:
    print("Your password is invalid")

