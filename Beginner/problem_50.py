# Problem 50
# Write A Python Program To Find Area Of Triangle formula: (base x height)/2

base, height = map(float, input("Enter the value (Base,Height): ").split(','))
print(f"Area of the triangle is: {(base*height)/2}")