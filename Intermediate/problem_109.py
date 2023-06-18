# Problem 109
# Write A Python Program To Get A Email From The User And Make Sure
# That It Is Email In Proper Format Having @ Symbol And@
import re
email = input("Enter your email: ")
if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
    print("Valid Email..")
else:
    print("Invalid Email..")