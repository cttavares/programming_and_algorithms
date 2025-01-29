import numpy as np

a = float(input("Enter the starting point (in radians): "))
b = float(input("Enter the ending point (in radians): "))

area = np.sin(b) - np.sin(a)
print("Area between the two points of the cos function: ", area)
