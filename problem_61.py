# Problem 61
# Write A Python Program To Get Memory In GB Then Convert GB In To Bytes
memory_size = int(input("Memory Size in GB: "))
memory_in_bytes = (memory_size*pow(1024, 3))
print(f"Memory size in byte: {memory_in_bytes}")