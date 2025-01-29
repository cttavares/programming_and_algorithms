def is_prime (n):
    
    for i in range (1, n-1):
        if n % (n-i) == 0:
            return False

    return True

n = int (input ("Write n: "))
print ("Is prime: ", is_prime (n))