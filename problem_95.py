# Problem 95
# Write Python Program To Find Force Of A Man On A Object Which Have
# Mass And Acceleration. Get Mass And Acceleration From User
# Formula:
# F = mass * acceleration (ma)
mass = int(input("Enter the mass: "))
acceleration = int(input("Enter the acceleration: "))
force = float(mass*acceleration)
print(f"Force = {force} kg-m/s²")

