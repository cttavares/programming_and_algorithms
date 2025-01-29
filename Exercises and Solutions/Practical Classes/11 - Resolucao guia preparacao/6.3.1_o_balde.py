import itertools
import time

l = [("F", 5), ("T", 2), ("D", 10)]

solucoes = []

def sequencia_accoes_e_valida (i):
    frente = 2
    for j in i:
        if j [0] == "D":
            frente = 6
        elif j [0] == "F":
            frente = frente - 1
        else:
            frente = 2
        
        if frente < 0:
            return False
    
    return True


def distancia_percorrida (i):
    distancia = 0
    for j in i:
        if j [0] == "D":
            distancia -= 10
        elif j [0] == "F":
            distancia += 5
        else:
            distancia -= 2
    
    return distancia


def distancia_e_percorrida (i, distancia_objectivo):
    return distancia_percorrida (i) == distancia_objectivo


def verify_solution (i, d):
    return sequencia_accoes_e_valida (i) and distancia_e_percorrida (i, d) 

def solucao_brute_force (distancia_objectivo, numero_passos):
    for i in itertools.product (l, repeat=numero_passos):
        if verify_solution (i, distancia_objectivo) == True:
            solucoes.append (i)        

    print ("Solucoes: ", solucoes)

def solucao_com_backtracking (distancia_objectivo, accoes = []):
    print ("Accoes: ", accoes)
    time.sleep (1)    
    if not sequencia_accoes_e_valida (accoes):
        print ("Invalida! ", accoes)
        return []
    
    distancia_p = distancia_percorrida (accoes)
    print ("Distancia percorrida: ", distancia_p)
    
    if distancia_p != distancia_objectivo:
        solucao = []
        for i in l:
            if i [0] == "F" and distancia_p > distancia_objectivo:
                continue
            
            res = solucao_com_backtracking (distancia_objectivo, accoes + [i])
            if  res != []:
                solucao = res
                break
        return solucao
    
    else:
        return accoes
    

print ("Solucoes: ", solucao_com_backtracking (60))
#print ("Solucao brute force: ", solucao_brute_force (60, 25))
