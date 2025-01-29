a = float (input ("Write a: "))
b = float (input ("Write b: "))
t = int (input ("Write the time t:"))

r_a = 2/(a**2)
r_b = 2/(b**2)

position_a_t = -(9.75 * (t**2)*r_a)/2
position_b_t = -(9.75 * (t**2)*r_b)/2
position_b_x_t = 3 * t

d = (abs (position_a_t - position_b_t)**2 + abs (position_b_x_t**2))**0.5
print ("Distance is: ", d)
