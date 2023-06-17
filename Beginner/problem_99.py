# Problem 99
# Write A Python Program To Get Only Uppercase Words From User To Store in A List
word = [input("Word: ") for _ in range(10)]
upperList = []
for wd in word:
    if wd.isupper():
        upperList.append(wd)
    else:
        continue
print(upperList)