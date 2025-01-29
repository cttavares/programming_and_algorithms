n1 = 10
n2 = 12
n3 = 13

if n1 > n2:
   maior = n1
   menor = n2
else:
   maior = n2
   menor = n1

if n3 > maior:
   medio = maior
   maior = n3
elif n3 < menor:
    medio = menor
    menor = n3
else:
   medio = n3

print ("Maior:", maior, ";Medio", medio, ";Menor", menor)