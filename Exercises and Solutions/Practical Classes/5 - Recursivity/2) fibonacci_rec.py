def fib_rec (n):
    if n == 0:
        return 0
    
    if n == 2 or n == 1:
        return 1
    else:
        return fib_rec (n-2) + fib_rec (n-1)

print ("Fibonacci: ", fib_rec (20))