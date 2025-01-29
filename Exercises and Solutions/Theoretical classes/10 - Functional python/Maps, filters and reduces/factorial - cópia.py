from functools import reduce

def product (a, b):
    return a*b

n = 3
fact = reduce (product, range (1, n+1))
print ("Factorial: ", fact)