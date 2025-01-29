from functools import cache

contador = 0

#@cache
def fib (n):
    global contador
    contador = contador + 1
    
    if (n <= 2):
        return 1
    
    return fib (n-1) + fib (n-2)

print (fib (40))
print ("Numero de chamadas: ", contador)