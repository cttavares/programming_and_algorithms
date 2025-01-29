intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]

def intersect_lists (l1, l2):
    inter = []
    for i in l1:
        if i in l2:
            inter.append (i)
    
    return inter

def intersect (i1, i2):
    # A very simplistic way of intercepting

    l1 = [i for i in range (i1[0], i1[1]+1)]
    l2 = [i for i in range (i2[0], i2[1]+1)]

    li = intersect_lists (l1, l2)
    if li == []:
        return [i1,i2]
    else:
        return [(l1 [0], l2 [-1])]
    
i = 0
result = []
while i < len (intervals):
    j = i + 1
    while j < len (intervals):
        r_int = intersect (intervals [i], intervals [j])
        print ("R_int: ", r_int)
        
        for r_i in r_int:
           if r_i not in result:
                result += r_i        
        
        
        j = j + 1
    
    i = i + 1

print (result)