import numpy as np

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

r = np.sqrt(x**2 + y**2)
theta = np.degrees(np.arctan2(y, x))

print("Polar coordinates (r, θ): (", r,",", theta, "degrees)")