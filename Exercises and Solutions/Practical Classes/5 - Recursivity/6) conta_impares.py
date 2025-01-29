def conta_impares_e_divisiveis_por_3 (x, y):
    if x > y:
        return 0
    
    # A utilização directa do resultado da condição
    # simplifica grandemente o código 
    return (x % 3 == 0 and x % 2 != 0) + conta_impares_e_divisiveis_por_3 (x+1, y)

print ("Conta impares: ", conta_impares_e_divisiveis_por_3 (1, 10))