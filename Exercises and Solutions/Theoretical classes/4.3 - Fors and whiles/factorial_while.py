factorial = 1 
n = 3

while n >= 1:
    # As seguintes expressões são iguais
    factorial = factorial * n
    factorial*=n 
    
    n=n-1

print ("Factorial: ", factorial)