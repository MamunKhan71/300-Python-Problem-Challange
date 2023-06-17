# Problem 31
"""
a Write A Python Program To Get Marks Of Student To Find Its Grade
Using This Criteria
>=95 Show A+ Grade
Show A Grade
show B Grade
Show C Grade
Lower Than 60, Will Be Fail Consider
"""

print("A+" if (number := int(input("Enter Your Grade: "))) >= 95 else "A" if 80 <= number < 95 else "B" if 70 <= number < 80 else "C" if 60 <= number < 70 else "F")
