# Problem 31_1
"""
Write A Python Program To Get Scale From Employer And
Then Display Salary According To Employer Scale
Using This Criteria, If:
Scale Is 9, display 10,000
Scale Is 12 , display 20,000
Scale Is 15 ,
display 40,000
Scale Is 18 , display 50,000
Scale Is 20
display 70,000
"""

print("10,000" if (numbers := input("Enter Your Scale: ")) == "9" else "20,000" if numbers == "12" else "40,000" if numbers == "15" else "50,000" if numbers == "18" else "70,000" if numbers == "20" else "Scale Not Found")