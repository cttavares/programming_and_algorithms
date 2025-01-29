from numpy import floor, log10

# Função de contagem de digitos para numeros inteiros
# positivos

def conta_digitos_com_matematica (n):
    if n < 1:
        return 1
    return (int (floor (log10 (n)))+1)

def conta_digitos (n):
    if n < 10:
        return 1
    else:
        return 1 + conta_digitos (n//10)

print ("Contagem: ", conta_digitos (12345))
print ("Contagem com matematica: ",  conta_digitos_com_matematica (12345))

print ("Contagem: ", conta_digitos (-23))
print ("Contagem com matematica: ",  conta_digitos_com_matematica (-23))