def sum (a, b):
    return a + b

def mult (a,b):
    return a * b

def apply (f, a, b):
    return f (a, b)

def combine (f, g, a, b, c):
    return apply (g, f (a, b), c)

n1 = int (input ("Escreva operando 1: "))
n2 = int (input ("Escreva operando 2: "))
n3 = int (input ("Escreva operando 3: "))
op = input ("Escreva operacao: ")

f = sum
g = mult

if op == "+":
    a = sum
else:
    a = mult

print ("O resultado da operacao é: ", apply (a, n1, n2))
print ("O resultado do combine é: ", combine (g, f, n1, n2, n3))       
       
       
