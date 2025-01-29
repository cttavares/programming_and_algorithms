def factorial(n):
    if n < 2:
        return 1
    
    n_1 = 1
    n_2 = 1
    for i in range (2, n+1):
        current = n_1 + n_2
        n_1 = n_2
        n_2 = current
    
    return current

n = int (input ("Write n: "))
print ("Factorial is: ", factorial (n))