import random
n = [i for i in range (0, 10)]

s = len (n) 


if s % 2 == 0:
    # No caso de ser 10, s//2 da 5 e s//2 - 1 sera 4, 
    # os dois elementos centrais da lista
    print ("n1: ", n [s//2], " n2: ", n [(s//2)-1])
    m = n [s//2] + n [(s//2)-1] / 2
else:
    m = n [s//2]

print ("A mediana da lista é: ", m)