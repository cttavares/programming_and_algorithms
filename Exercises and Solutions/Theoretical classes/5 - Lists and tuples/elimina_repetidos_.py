lista = [1,2,2, 3, 4, 5, 5]

def com_lista_auxiliar_ (l):
    global lista
    
    lista_auxiliar = []

    for i in l:
        if i not in lista_auxiliar:
            lista_auxiliar.append (i)
    
    # Isto ano functiona!
    lista = lista_auxiliar 

    #l.clear ()
    #for i in lista_auxiliar:
    #    l.append (i)

def com_lista_auxiliar (l):
    lista_auxiliar = []

    for i in l:
        if i not in lista_auxiliar:
            lista_auxiliar.append (i)
    
    return lista_auxiliar


#lista = com_lista_auxiliar (lista)
com_lista_auxiliar_ (lista)
print ("Lista: ", lista)
