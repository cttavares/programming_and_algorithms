def soma (a, b):
    #if a == 0 and b == 0:
    #    return 1
    
    return a+b 

def multiplica (a,b):
    return a*b

a = int (input ("Escreva numero: "))
b = int (input ("Escreva numero: "))
print ("Soma e multiplica: ", soma (multiplica (a,b),b))

