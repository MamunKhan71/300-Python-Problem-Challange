# Problem 16
# Write A Program That Performs All Compound Assignment Operations On An Integer

"""
Compound Operators:
+=
-=
*=
/=
"""
sum = 0
num = int(5)
num += 4
sum += num
print(f"Compound Sum : {num}")
num -= 4
sum += num
print(f"Compound Sub : {num}")
num *= 5
sum += num
print(f"Compound Mul : {num}")
num /=5
sum += num
print(f"Compound Div : {num}")

print(f"Sum : {sum}")