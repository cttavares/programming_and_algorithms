
lista = [1,2,2, 3, 4, 5, 5]

def elimina_repetidos_for ():
    lista_add = []
    for i in lista:
        if i not in lista_add:
            lista_add.append (i)
    return lista_add

def elimina_repetidos_com_algo (l1):
    print (l1)
    i = 0
    while i < len (l1):
        action = True
        while action == True:
            if l1.count (l1 [i]) > 1:
                l1.remove (l1[i])
            else:
                action = False
                i = i + 1

    return l1        

def elimina_repetidos_com_sort (l):
    l.sort ()
    i = 0
    while (i < len (l)):
        j = i + 1
        if j < len (l) and l [j] == l [i]:
            l.pop (j)
        else:
            i = i + 1
    return l

def elimina_recursivo (lista):
    if lista == []:
        return []
    
    if lista [0] not in lista [1:]:
        return [lista [0]] + elimina_recursivo (lista [1:])
    else:
        return elimina_recursivo (lista [1:])
    

print ("Imprime lista: ", elimina_recursivo ([1,1,1,2, 3, 3, 4, 4, 4]))
print ("Lista sem repetidos: ", elimina_repetidos_for ())
print ("Imprime lista com algo ", elimina_repetidos_com_algo ([1,1,1,2, 3, 3, 4, 4, 4]))
print ("Imprime lista com sort", elimina_repetidos_com_sort ([1,1,1,2, 3, 3, 4, 4, 4]))