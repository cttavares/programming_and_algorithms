l = [2, 3, 5, 7, 8, 1, 0, -1]

def min_recursive (l):
    if len (l) == 1:
        return l [0]
    else:
        m = min_recursive (l [1:])
        if m < l [0]:
            return m
        return l [0]

print ("Min: ", min_recursive (l))