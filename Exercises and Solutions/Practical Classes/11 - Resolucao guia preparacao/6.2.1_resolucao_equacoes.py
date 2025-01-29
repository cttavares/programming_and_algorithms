import itertools

As = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
Bs = [3, 3, 3]

x = [i for i in range (1, 10)]

def verifica_solucao (s):
    for j, l in enumerate (As):
        if sum (map  (lambda i: l[i]*s [i], range (0,3))) != Bs [j]:
            return False
    
    return True

for i in itertools.product (x, repeat = 3):
    if verifica_solucao (i):
        print ("Solucao possivel: ", i)