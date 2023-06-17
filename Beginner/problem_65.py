# Problem 65
# Write A Python Program To Find Area And Perimeter Of A Square Using Function
import math

square_param = int(input("Enter the number: "))
area = pow(square_param,2)
perimeter = 4*square_param
print(f"Area : \t\t\t\t{area}\nPerimeter : \t\t{perimeter}")
print(f"Sqrt Area : \t\t{math.sqrt(area)}\nSqrt Perimeter : \t{math.sqrt(perimeter)}")
