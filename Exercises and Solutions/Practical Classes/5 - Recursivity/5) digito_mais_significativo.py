# O digito mais significativo e o 
# digito que representa a maior potencia,
# ou seja, o digito mais a esquerda do número.
# Exemplo: Em 1234 o digito mais significativo e o 1
def most_significant (n):
    if n < 10:
        return n
    else:
        return most_significant (n//10)

print ("Most significant:", most_significant (899))