import itertools
from functools import reduce

lw = [(1, 20), (2, 30), (3, 10), (4, 5), (5, 50)]

W_limit = 50

def is_valid (solution):
    print (solution)
    return sum (map (lambda x: x[1], solution)) < W_limit

def score (solution):
    return sum (map (lambda x: x [0], solution))

best_score_and_solution = (0, ())
for j in range (1, len (lw)+1):
    for i in filter (is_valid, itertools.combinations (lw, j)):
        print ("Score for ", i, " is ", score (i))
        if score (i) > best_score_and_solution [0]:
            best_score_and_solution = (score (i), i)

print ("Best score and solution: ", best_score_and_solution)
