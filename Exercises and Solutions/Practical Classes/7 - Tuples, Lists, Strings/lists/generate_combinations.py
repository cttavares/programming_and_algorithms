import itertools

l = [i for i in range (1, 11)]

r = []
for i in itertools.combinations (l, 3):
    r.append (i)

print (r)