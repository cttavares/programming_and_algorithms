def collatz (n):
    counter = 1
    while (n != 1):
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        counter = counter + 1
    
    return counter 

n = int (input ("Write n: "))
print ("Collatz is ", collatz (n))