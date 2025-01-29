import numpy as np

angle_deg = float(input("Enter the angle in degrees: "))
print("Cosine:", np.cos(np.radians(angle_deg)))
print("Sine:", np.sin(np.radians(angle_deg)))
print("Tangent", np.tan(np.radians(angle_deg)))
