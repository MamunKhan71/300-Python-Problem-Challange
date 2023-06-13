# Problem 46
"""
Write A Python Program To Get 5.Subject Marks, Store Them Into Array, And Also Get Student Name. Find Total
And Display Each Subjects Marks.
Expected result:
Hi username!
Your marks is ......
See your all subject marks
English = ...
Physics = ...
Computer = ...
Math: ...
"""
from array import array
name = input("Enter Your Name : ")
sub_marks = array('i', [int(input("Enter Your Number: ")) for _ in range(5)])
print(f"Hi {name}!\nYour marks is : {sum(sub_marks)}\nSee your all subject marks\nEnglish = {sub_marks[0]}\nPhysics = {sub_marks[1]}\nComputer = {sub_marks[2]}\nMath = {sub_marks[3]}")