def cubo (e):
    return e * e * e

def map_i (f, C):
    r = [f (i) for i in C]
    return r

r = [i for i in range (1, 101)]
lr = map_i (cubo, r)

for j in lr:
    print ("Cubos: ", j)