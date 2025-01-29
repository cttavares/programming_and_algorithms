def conta_digitos (n):
    if n < 10:
        return 1
    else:
        return 1 + conta_digitos (n//10)

def inverte_digitos (n):
    if n < 10:
        return n % 10
    else:
        r = inverte_digitos (n//10)
        return (n % 10)*(10**(conta_digitos (r))) + r
    
print ("Inversao de digitos: ", inverte_digitos (1234))
print ("Digitos invertidos: ", inverte_digitos (985))