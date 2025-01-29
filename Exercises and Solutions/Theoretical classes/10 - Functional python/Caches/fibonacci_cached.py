from functools import cache

n_calls = 0
n_calls_non_rec = 0

@cache
def fibonacci (n):
    global n_calls 
    n_calls = n_calls + 1
    if n <= 2:
        return n
    return fibonacci (n-1) + fibonacci (n-2)


def fib (n):
    global n_calls_non_rec
    n_calls_non_rec = 1

    if n <= 2:
        return n
    
    f_0 = 1
    f_1 = 1
    
    for i in range (2, n):
        n_calls_non_rec = n_calls_non_rec + 1
        current = f_0 + f_1
        f_0 = f_1
        f_1 = current
    
    return current

N = 40
print (fib (N))
print ("Number of non-recursive calls", n_calls_non_rec)
print (fibonacci (N))
print ("Number of calls: ", n_calls)