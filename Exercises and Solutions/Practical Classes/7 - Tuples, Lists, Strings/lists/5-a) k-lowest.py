l = [9, 5, 4, 6, 7, 8, 8, 9, 9, 7, 7, 7, 7, 1, 2, 3]

def k_lowest (l, k):
    l.sort ()
    return l [0:k]

k = 5
print ("The k-lowest elements are: ", k_lowest (l, k))
