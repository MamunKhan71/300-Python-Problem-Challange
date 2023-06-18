# Problem 106 Write A Python Program To Get Password From The User That Contain Alpha Numeric And More Than 8 And
# Less Than 20 Characters

inpt = input("Enter Your Password(Alphanumeric and between 8&20 Chars: ")
if inpt.isalnum():
    if 8 < len(inpt) < 20:
        print("Your Password is Valid..")
    else:
        print("Sorry! Password must be between 8 to 20 characters long!")
else:
    print("Please Type Alpha Numeric Value only!")