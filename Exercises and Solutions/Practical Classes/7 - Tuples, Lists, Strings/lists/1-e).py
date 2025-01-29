l = [i for i in range (1,20)]

def swap (l, i, j):
    t = l [i]
    l [i] = l [j]
    l [j] = t
    return l

i = int (input ("Write first index: "))
j = int (input ("Write second index: "))
swap (l, i, j)
print ("New list: ", l)

