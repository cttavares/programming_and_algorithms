import numpy as np

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def approx_e (n):
    sum = 0
    for k in range (0, n):
        sum += 1 / factorial (k)
    
    return sum

n = int (input ("Write n: "))
print ("E is: ", approx_e (n))
