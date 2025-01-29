def conta_vezes (n, d):
    if n < 10:
        return n % 10 == d
    else:
        return (n % 10 == d) + conta_vezes (n//10, d) 
        
print ("Conta vezes: ", conta_vezes (100, 0))