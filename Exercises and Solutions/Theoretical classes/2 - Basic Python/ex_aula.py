GRAVITY = 9.8

def air_resistance (z):
    return 2/(z**2)

def free_fall (r,t):
    return (1/2)*(GRAVITY)*(t**2)*r

def distance (x_1, y_1, x_2, y_2):
    return (abs (x_2 - x_1)**2 + 
            abs (y_2 - y_1)**2)**0.5  

# Leitura dos dados
a = float (input ("Escreva a: "))
b = float (input ("Escreva b: "))
t = float (input ("Escreva t: "))
# Processamento dos dados
# Aqui estamos a calcular a resistencia do ar
r_a = air_resistance (a)
r_b = air_resistance (b)

s_a = free_fall (r_a, t)
s_b = free_fall (r_b, t)

d_b = 3*t
# Calcular a distancia final
d= distance (0, s_a, d_b, s_b)
# Escrita dos dados
print ("A distancia e d: ", d)