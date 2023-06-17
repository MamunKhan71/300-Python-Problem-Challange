# Problem 64
"""
Write A Python Program To Find Scholarship For Students In Admission
In A College On The Basis Of Student Marks.
Criteria To Follow
Marks Equal To 1100 - Free Education
Marks > 1000 - 80% Monthly Fees Deduction
Marks > 900 - 60% Monthly Fees Deduction
Marks > 800 - 40% Monthly Fees Deduction
Marks > 700 - 30% Monthly Fees Deduction
Marks > 600 - There Is No Scholarship
"""
marks = int(input("Enter your total marks: "))
print("Free Education" if marks == 1100 else "80% Monthly Fees Deduction" if 1000 <= marks <= 1099 else "60% Monthly Fees Deduction" if 900 <= marks <= 999 else "40% Monthly Fees Deduction" if 800 <= marks <= 899 else "30% Monthly Fees Deduction" if 700 <= marks <= 799 else "There Is No Scholarship")

