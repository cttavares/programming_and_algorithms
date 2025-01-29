from functools import reduce

# a => (elemento_anterior, soma_anterior)
def fib_red (a, b):
    return (a [1], a [1] + a [0])
    
def fibonacci (n):
    if n <= 2:
        return 1
    
    return reduce (lambda x, _: (x [1], x [0] + x [1]), map (lambda x: (1,2) if x == 3 else x, range (3, n+1)))[1]

n = 10
print ("Fibonacci: ", fibonacci (n))