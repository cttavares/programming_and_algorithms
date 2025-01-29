def flatten (l):
    if l == []:
        return l
    
    if isinstance (l [0], list):
        return flatten (l [0]) + flatten (l [1:])
    else:
        return [l [0]] + flatten (l [1:])


l = [[1,1,1], [[[2,3,3], [2,5,6]], 2, 5, 6], 4]

print ("Result list: ", flatten (l))