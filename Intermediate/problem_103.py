# Problem 104
# Write A Python Program To Get Any File With Extension, To Display Only That File Extension
import os.path

inpt = input("Enter the file name with extension: ")
file_name, file_extension = os.path.splitext(inpt)
print(f"The extension of the file is : {file_extension}")