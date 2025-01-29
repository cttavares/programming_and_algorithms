from some_functions import soma_numeros
from some_functions import multiplica_numeros
from some_functions import divide_numeros

x = float (input ("Escreva um numero: "))
y = float (input ("Escreva outro numero: "))
z = float (input ("Escreva ainda outro numero"))

sum_1 = soma_numeros (y, z)
sum_2 = soma_numeros (x, x) 

mul = multiplica_numeros (sum_1, sum_2)
divd = divide_numeros (mul, x)

print ("The crazy output of this progam is: ", divd)
