def mostra_elementos (n):
    print (n)
    if (n == 10):
        return
    else:
        mostra_elementos (n+1)

def soma_elementos (n):
    if (n==10):
        return 10
    else:
        return n + soma_elementos (n+1)

def multiplica_numeros (n, limite):
    if (n > limite):
        return 1
    else:
        if (n % 3 == 0):
            return n * multiplica_numeros (n+1, limite)
        else: 
            return multiplica_numeros (n+1, limite) 



#print ("Soma: ", soma_elementos (1))
print ("Multiplica numeros: ", multiplica_numeros (1, 6))
#mostra_elementos (1)