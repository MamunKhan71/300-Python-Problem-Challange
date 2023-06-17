# Problem 102
# Write A Python Program To Sort Student Name In Ascending Order In List And Student Should Display Which
# Contain Only 5 Character
shortList = []
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


name = ["Mamun", "Nahid", "Zarin", "Soha", "Fuad", "Farhan", "Limon"]
for nm in name:
    if len(nm) == 5:
        shortList.append(nm)
bubble_sort(shortList)
print(shortList)