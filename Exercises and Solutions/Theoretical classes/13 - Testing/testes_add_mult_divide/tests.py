from some_functions import soma_numeros 
from some_functions import multiplica_numeros
from some_functions import divide_numeros

assert (soma_numeros (10, 5) == 15)
assert (soma_numeros (500, 600) == 1100)
assert (soma_numeros (-1, -1) == -2)
assert (soma_numeros (0, 10) == 10)

assert (multiplica_numeros (20, 20) == 400)
assert (multiplica_numeros (-20, -20) == 400)
assert (multiplica_numeros (0, 0) == 0)

try:
    assert (divide_numeros (3, 0) == 0)
except ZeroDivisionError:
    assert (True)

assert (divide_numeros (45, 5) == 9)
