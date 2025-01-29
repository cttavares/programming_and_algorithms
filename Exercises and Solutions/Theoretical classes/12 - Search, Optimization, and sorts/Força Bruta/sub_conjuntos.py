import itertools
l = []

s = {1,2,3, 9, 7, 8, 10}
c = 2

for c in range (0, len (s)+1):
    for i in itertools.combinations (s, c):
        l.append (set (i))

print ("A lista de todos os conjuntos é: ", l)
