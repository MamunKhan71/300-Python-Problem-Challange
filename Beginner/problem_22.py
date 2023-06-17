# Problem 23
# Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant
import re
inp = input("Enter any letter: ")
if re.findall(r'[aeiouAEIOU]', inp):
    print("Vowel")
else:
    print("Consonant")
