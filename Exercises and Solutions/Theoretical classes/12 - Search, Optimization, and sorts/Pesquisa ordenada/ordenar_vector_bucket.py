# 7*3= 12 = N LOG N (LOG 7 arred para 3)
l =  [1, 3, 2, 7, 9, 11, 10]

# 12 - Python faz isto rapido?
v = [(i, False) for i in range (1,12)]

#print (v)
# 7 passos
for i in l:
    v [i-1] = (i, True)

lista_ordenada = []
# 12 passos
for i in v:
    if i [1] == True:
        lista_ordenada.append (i [0])

print (lista_ordenada)   