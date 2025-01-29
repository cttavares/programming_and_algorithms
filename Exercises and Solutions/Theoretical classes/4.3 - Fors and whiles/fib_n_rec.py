contador = 0

def fib_n_rec (n):
    var_minus_1 = 1     
    var_minus_2 = 1
    global contador
    contador = contador + 1
    if (n <= 2):
        return 1
    
    for _ in range (2, n):
        current = var_minus_2 + var_minus_1 
        var_minus_1 = var_minus_2 
        var_minus_2 = current
        contador = contador + 1
    
    return var_minus_2 

print (fib_n_rec (40))
print ("Numero de passos: ", contador)