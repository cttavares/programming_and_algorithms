cos_a = float(input("Enter cos of the first angle: "))
sin_b = float(input("Enter sin of the second angle: "))
cos_diff = float(input("Enter cos of the difference between the two angles: "))

# Using product-to-sum identity: cos(A-B) = cosAcosB + sinAsinB
# We have cosA and sinB, so we can estimate sinA
sin_a = (cos_diff - cos_a * sin_b) / sin_b

if sin_a > 0:
    print("The first angle is in the first or second quadrant (positive sine value).")
else:
    print("The first angle is in the third or fourth quadrant (negative sine value).")
