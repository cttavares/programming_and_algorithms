l = [1, 3, 2, 7, 9, 11, 10]
passos = 0

def binary_search_recursive(lst, target): 
    global passos
    passos = passos + 1

    if len(lst) == 0:
        return -1
    
    mid = len(lst) // 2
    
    # Verifica se o elemento está no meio if lst[mid] == target:
    print ("Elemento do meio", lst [mid])
    if lst[mid] == target:
        return lst [mid]
    
    if lst [mid] > target:
        return binary_search_recursive (lst [:mid], target)
    else:
        return binary_search_recursive (lst [mid+1:], target)

l.sort ()
e = binary_search_recursive (l, 2)
print ("Elemento encontrando: ", e) 
print ("numero de passos: ", passos)
