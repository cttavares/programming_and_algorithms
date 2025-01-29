l = [9, 5, 4, 6, 7, 8, 8, 9, 9, 7, 7, 7, 7, 1, 2, 3]

def elimina_recursivo (l, n):
    if l == []:
        return []
    
    if l [1:].count (l [0]) < n:
        return [l [0]] + elimina_recursivo (l [1:], n)
    else:
        return elimina_recursivo (l [1:], n)

n = 1
l = elimina_recursivo (l, n)
print ("Lista sem repetidos:" ,l)