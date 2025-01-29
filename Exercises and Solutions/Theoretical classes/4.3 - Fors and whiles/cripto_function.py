a= 1000000
n = 1234
X_k_1 = 1

def gera_numero ():
    global X_k_1
    X_k = (a * X_k_1) % n
    X_k_1 = X_k
    return X_k

for i in range (0,  10):
    print (gera_numero ())