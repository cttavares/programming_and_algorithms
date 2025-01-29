import time
import random
import os

estado = []

LIM_LATERAL = 30
LIM_SUPERIOR = 15

def nova_lista ():
    return [["\033[96m" + "█" + "\033[0m" for i in range (0, LIM_LATERAL)] for _ in range (0, LIM_SUPERIOR)]

def mostra_cenario (estado):
    lista = nova_lista ()

    for i in estado:
        lista [i [1]][i [0]] = "🛬"

    print ("\r")  
    for i in range (len (lista)):
        for j in range (len (lista [i])):
            print (lista [i][j], end="")
        print ("\r")
    print ("")

def visualiza_estado (estado):
    os.system('cls' if os.name == 'nt' else 'clear')
    mostra_cenario (estado)
    

def altera_aviao (i, novo_x, novo_y, novo_v_x, novo_v_y):
    if i < len (estado):
        estado [i] = (novo_x, novo_y, novo_v_x, novo_v_y)
    else:
        estado.append ((novo_x, novo_y, novo_v_x, novo_v_y))
    
    return

def calcula_nova_posicao (i):
    novo_x = estado [i][0] + estado [i][2]
    novo_y = estado [i][1] + estado [i][3]

    if (novo_x >= LIM_LATERAL):
        novo_x = novo_x % LIM_LATERAL
    elif novo_x < 0:
        novo_x = LIM_LATERAL + novo_x

    if (novo_y >= LIM_SUPERIOR):
        novo_y = novo_y % LIM_SUPERIOR
    elif novo_y < 0:
        novo_y = LIM_SUPERIOR + novo_y
    
    altera_aviao (i, novo_x, novo_y,  estado [i][2], estado [i][3])

def inicia ():
    altera_aviao (0, 1, 1, 1, 2)
    altera_aviao (1, 3, 3, 1, 3)
    altera_aviao (2, 6, 5, 3, 1)
    #pass

LIMITE_TEMPO = 30
t = 0 
inicia ()
while (t < LIMITE_TEMPO):
    visualiza_estado (estado)
    
    time.sleep (1)
    for index in range (len (estado)):
        calcula_nova_posicao (index)
        
    t = t + 1