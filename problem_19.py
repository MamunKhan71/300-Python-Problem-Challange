# Problem 19
# Write A Python Program To Get 3 Number From User And Put In The Following Equation:
# a+b+ca/b(2a + 3b)

a, b, c = map(int, input("Enter Your Number(a,b,c) : ").split(','))
print(float(a + b + c * a / b*(2 * a + 3 * b)))
