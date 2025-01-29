import itertools

As = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
Bs = [3, 3, 3]
Vs = [1.5, 6.7, -2.3]

x = [i for i in range (-20, 20)]

def score (s):
    return sum (map (lambda i: Vs [i]* x[i], range (0, 3)))

def verifica_solucao (s):
    for j, l in enumerate (As):
        if sum (map  (lambda i: l[i]*s [i], range (0,3))) > Bs [j]:
            return False
    
    return True

primeira_vez = True
best_sol = tuple ()

for i in itertools.combinations (x, 3):
    
    for j in itertools.permutations (i):
        if verifica_solucao (j):
            print ("Possivel solucao:", j)
            score_ = score (j)
            
            if primeira_vez or score_ < best_score:
                best_score = score_
                best_sol = i
                primeira_vez = False
        
print ("Solucao minima: ", best_sol)