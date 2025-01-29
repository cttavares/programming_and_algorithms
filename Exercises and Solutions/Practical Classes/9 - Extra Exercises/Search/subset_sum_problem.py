import itertools
import functools

s = {i for i in range (1, 10)}

N = 10

def verify_sum (s, n):
    if len (s) >= 1 and functools.reduce (lambda x,y: x+y, s) == n:
        return True
    else:
        return False

all_sets = []
for j in range (0, len (s)):
    for i in itertools.combinations (s, j):
        if verify_sum (i, N):
            all_sets.append (i)

for i in all_sets:
    print ("Set: ", i)