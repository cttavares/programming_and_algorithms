import itertools

l = [i for i in range (1, 10)]
r = []

for i in range (0, len (l)):
    for i in itertools.combinations (l, i):
        r.append (i)

print (r)