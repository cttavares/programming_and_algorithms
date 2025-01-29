from functools import reduce

def soma (n):
    return reduce (lambda x, y: x+y, range (1, n+1))

def factorial (n):
    return reduce (lambda x, y: x*y, range (1, n+1))

n = 6
print ("S: ", soma (n))

print ("Factorial: ", factorial (n))