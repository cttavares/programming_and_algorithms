l = [2, 3, 5, 7, 8, 1, 0, -1]


def min_e_max_com_while ():
    min = l [0]
    max = l [0]

    j = 0

    while j < len (l):
        if l [j] > max:
            max = l [j]        
        if l [j] < min:
            min = l [j]
        
        j = j + 1
    
    return (min, max)


def min_e_max_with_for ():
    min = l [0]
    max = l [0]
    
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i

    return (min, max)


def max_with_for ():
    max = l [0]
    for i in l:
        if i > max:
            max = i
    
    return max


def min_with_for ():
    min = l [0]
    for i in l:
        if i < min:
            min = i
    
    return min

def min_with_sort ():
    l.sort ()
    return l [0]

#def recursive_min (l):
#    recursive_min ()


#print (min_with_for ())
print ("Min: ", min_with_sort ())
print ("Max: ", max_with_for ())
#print ("Min e max:", min_e_max_with_for ())
print ("Min e max:", min_e_max_com_while ())
