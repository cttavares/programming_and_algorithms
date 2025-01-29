l = [9, 5, 4, 6, 7, 8, 8, 9, 7, 7, 1, 2, 3]

def elimina_recursivo (l):
    if l == []:
        return []
    
    if l [0] not in l [1:]:
        return [l [0]] + elimina_recursivo (l [1:])
    else:
        return elimina_recursivo (l [1:])

def elimina_standard (l):
    # "Standard" solution
    index = 0
    for i in l:
        if l [index] in l [index + 1:]:
            l.remove (l [index]) 
        else: 
            index = index + 1

def elimina_com_lista_auxiliar (l):
    # Solucao elegante, apenas adicionar elementos
    # a uma lista adicional desde que eles não existam na mesma
    lr = []
    for i in l:
       if i not in lr:
           lr.append (i)
    
    l.clear ()
    for i in lr:
        l.append (i)

def elimina_com_sort (l):
    # Solution using sort
    l.sort ()
    i = 0
    j = 0
    while j < len (l):
        i = j
        while i < len (l):
            if (i + 1 < len (l) and l [i] == l [i+1]):
               l.pop (i+1)
            i = i + 1
        j = j + 1

# Another solution using sort
def eliminat_com_sort_alternativo (l):
    l.sort ()
    i = 0
    j = 0
    while j < len (l):
        i = j
        while i + 1 < len (l) and l [i] == l [i+1]:
            l.pop(i+1)
        j = j + 1

print (l)
#elimina_standard (l)
#elimina_com_lista_auxiliar (l)
#elimina_com_sort (l)
#eliminat_com_sort_alternativo (l)
l = elimina_recursivo (l)

print ("Lista sem repetidos:" ,l)


