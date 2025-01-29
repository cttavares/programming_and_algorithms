import itertools

stocks = [(12, 0.9), (3, 0.01), (5, 0.3), (19, 0.84), (2, 0.001)]
N = 3
maximum_risk = 1.5

def is_valid (s):
    soma = 0
    for i in s:
        soma += i [1]

    if soma <= maximum_risk:
        return True
    else:
         return False

def score (s):
    score_ = 0

    for i in s:
        score_ += i [0]
    
    return score_

score_max = 0
solucao = tuple ()

for i in filter (is_valid, itertools.combinations (stocks, N)):
    if score (i) > score_max:
        solucao = i
    
print ("A solucao é: ", solucao)
