def sum (a, b):
    return a + b

def mult (a,b):
    return a * b

n1 = int (input ("Escreva operando 1: "))
n2 = int (input ("Escreva operando 2: "))
op = input ("Escreva operacao: ")

if op == "+":
    f = sum
elif op == "*":
    f = mult

print ("O resultado da operaacao sera: ", f (n1, n2))