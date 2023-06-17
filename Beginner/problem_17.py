"""
Write a Python program to show a message in this format using print function. Each character should one tab distance
A
B   C
D   E   F
G   H   I   J
K   L   M
N   O
P
"""
from itertools import chain

char = 65

for i in chain(range(4), range(2, -1, -1)):
    num_chars = i + 1
    chars = [chr(char + j) for j in range(num_chars)]
    print("\t".join(chars))
    char += num_chars
