# Problem 112
# Write A Python Program To Find Gravitational Force
#  GF = (Gravitational Constant × Mass of first object × Mass of the second object) / (Distance between the centre of two bodies)^2

first_object = float(input("Enter the mass of the first object: "))
second_object = float(input("Enter the mass of the second object: "))
distance = float(input("Enter the distance between two objects: "))
print(6.674*pow(10, -11))
gF = ((6.674*pow(10, -11))*first_object*second_object)/pow(distance, 2)
print(f"Gravitational Force: {gF} Newton")