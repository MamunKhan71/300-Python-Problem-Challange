# Problem 17_1
"""
# Program to print the following:

A
B	C
D	E	F
G	H	I	J
K	L	M	N	O
P	Q	R	S	T	U

"""
from itertools import chain

char = 65

for i in chain(range(6)):
    numChar = i + 1
    chars = [chr(char + j) for j in range(0, numChar)]
    print("\t".join(chars))
    char += numChar