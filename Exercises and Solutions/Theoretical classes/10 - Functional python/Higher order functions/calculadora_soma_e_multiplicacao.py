# (A+B)*C

def sum (a, b):
    return a + b

def mult (a,b):
    return a * b

def soma_and_multiply (a, b, c):
    return sum (a,b) * c

def soma_and_multiply (a, b, c):
    return sum (mult (a,b),c)

def apply (f, a, b):
    return f (a, b)

def combine (f, g, a, b, c):
    return apply (g, f (a, b), c)

n1 = int (input ("Escreva operando 1: "))
n2 = int (input ("Escreva operando 2: "))
n3 = int (input ("Escreva operando 3: "))

print ("O resultado do combine é: ", combine (mult, sum, n1, n2, n3)) 

