l = [12,13,14,14,15,16,16]

        
r = []
for i in set (l):
    if l.count (i) > 1 and i not in r:
        r.append (i)

print ("Lista de repetidos: ", r)    