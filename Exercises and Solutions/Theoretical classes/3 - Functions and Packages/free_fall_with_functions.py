
def calculate_mass (o):
    return (o**3)/2

def calculate_free_fall_position (m, t):
    return -(9.81 * (t**2)*m)/2

def calculate_distance (x_1, y_1, x_2, y_2):
    return (abs (x_1 - x_2)**2 + abs (y_1 - y_2)**2)**0.5

a = int (input ("Write a: "))
b = int (input ("Write b: "))
t = int (input ("Write the time t:"))

m_a = calculate_mass (a)
m_b = calculate_mass (b)

position_a_t = calculate_free_fall_position (m_a, t)
position_b_t = calculate_free_fall_position (m_b, t)

distance = calculate_distance (0, position_a_t, 5*t, position_b_t)
print ("Distance is: ", distance)

