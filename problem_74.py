# Problem 74
# Write A Python Program To Find The Second Position Of A Student In A List And Display Marks
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


pos = [input("Marks: ") for _ in range(5)]
bubble_sort(pos)
print(f"Second Highest : {pos[1]}")
