import itertools
import functools

stocks = [(12, 0.9), (3, 0.01), (5, 0.3), (19, 0.84), (2, 0.001)]
N = 3
maximum_risk = 1.5

def is_valid_solution (set_of_stocks):
    risk = functools.reduce (lambda x, y: x + y, map (lambda x: x [1], set_of_stocks))
    
    if risk > maximum_risk:
        return False
    else:
        return True

def score (set_of_stocks):
    return functools.reduce (lambda x, y: x + y, map (lambda x: x [0], set_of_stocks))

maximum_score = 0

for i in itertools.combinations (stocks, 3):
    #print (i)
    if is_valid_solution (i) and score(i) > maximum_score:
        maximum_score = score (i)
        best_solution = i

print ("Best solution: ", best_solution)
        