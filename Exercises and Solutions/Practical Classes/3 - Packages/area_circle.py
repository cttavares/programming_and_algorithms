import numpy as np

radius = float(input("Enter the radius of the circle: "))
area = np.pi * (radius ** 2)
area = round (area, 2)
print(f"Area of the circle: ", area)
