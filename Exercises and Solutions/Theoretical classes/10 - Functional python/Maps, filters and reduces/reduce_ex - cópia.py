from functools import reduce

def cubo (a):
    return a*a*a

def soma (a, b):
    return a+b

r = reduce (soma, map (cubo, range (1,101)))
print ("R: ", r)