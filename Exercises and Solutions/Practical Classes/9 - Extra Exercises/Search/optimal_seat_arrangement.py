import itertools
import functools

preferences = {"P1": [1,2,3,4], "P2": [2, 3, 1, 4], 
               "P3": [3, 4, 1, 2], "P4": [4, 1, 3, 2]}

solution = {"P1", "P2", "P3", "P4"}

def score_solution (s):
    return (s, preferences [s [0]][0] + preferences [s [1]][1] + preferences [s [2]][2] + preferences [s [3]][3])

max = functools.reduce (lambda x, y: x if x [1] > y [1] else y, map (score_solution, itertools.permutations (solution)))
print ("Best solution:", max)