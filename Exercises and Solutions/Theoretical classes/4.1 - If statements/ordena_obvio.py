n1 = 10
n2 = 12
n3 = 13

if n1 < n2 and n2 < n3:
    print ("Ordenados: ", n1, ";", n2, ";", n3)
elif n1 > n2 and n1 < n3:
    print ("Ordenados: ", n2, ";", n1, ";", n3)
elif n3 < n1 and n1 < n2:
    print ("Ordenados: ", n3, ";", n1, ";", n2)
elif n2 < n3 and n3 < n1:
    print ("Ordenados: ", n2, ";", n3, ";", n1)
elif n1 < n3 and n3 < n2:
    print ("Ordenados: ", n1, ";", n3, ";", n2)
elif n3 < n2 and n2 < n1:
    print ("Ordenados: ", n3, ";", n2, ";", n1)
