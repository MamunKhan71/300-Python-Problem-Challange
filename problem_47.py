# Problem 47
"""
Write A Python Program To Get 2 Number From The User, Find Their
Square , And Add Both Result, Finally Result Display To User.
"""
num1, num2 = map(int, input("Numbers(separate by comma): ").split(','))
print(pow(num1, 2) + pow(num2, 2))