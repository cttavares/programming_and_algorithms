def remove (element, l):
    for i, v in enumerate (l):
        if v == element:
            return l [:i] + l [i+1:]
    return l 

l = [1,3,2,4,4,5,4]
print ("Len: ", remove (3, l))