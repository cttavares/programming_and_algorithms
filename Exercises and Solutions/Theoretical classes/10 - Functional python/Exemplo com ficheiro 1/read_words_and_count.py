from functools import reduce

def join_dictionaries (x,y):
        for i in x:
            if i not in y:
                y [i] = x [i]
            else:   
                y [i] += x [i]
        return y

with open ('words.txt', 'r') as file:
    r = reduce (join_dictionaries, map (lambda x: reduce (join_dictionaries, map (lambda y: {(y.strip(".,")).lower() : 1}, x)), [line.split() for line in file]))

    for i in r:
        print ("Word ", i, " freq", r [i])

