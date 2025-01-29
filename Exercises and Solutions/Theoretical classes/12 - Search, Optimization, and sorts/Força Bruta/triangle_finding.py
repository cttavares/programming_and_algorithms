from itertools import permutations
from numpy import sqrt


def distancia (p1, p2):
    print ("p1: ", p1)
    print ("p2: ", p2)
    print ("Distancia: ", sqrt (abs (p1 [0]- p2[0])**2 + abs (p1[1]-p2[1])**2))
    return sqrt (abs (p1 [0]- p2[0])**2 + abs (p1[1]-p2[1])**2)


def encontra_solucao (points):

    solucao = []
    for i in points:
        for j in points:
            for h in points:
                print ("-----")
                for p in permutations (d):
                    print ("P: ", p)
                    
                    if distancia (i, j) == p [0] and distancia (j, h) == p [1] and distancia (h,i) == p [2]:
                        solucao.append (i)
                        solucao.append (j)
                        solucao.append (h)
                        return solucao
    return solucao

d = (1, 1, 1)
points = [(2,3), (4,5), (6,7), (8,9), (10, 11)]

print ("Solucao: ", encontra_solucao (points))