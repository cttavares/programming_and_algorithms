l = [9, 5, 4, 6, 7, 8, 8, 9, 9, 7, 7, 7, 7, 1, 2, 3]

t = []
i = 0 
while i < len (l):
    j = i + 1
    while j < len (l):
        h = j + 1
        while h < len (l):
            t.append ((l [i], l [j], l [h]))
            h = h + 1
        j = j + 1
    i = i + 1

print ("All combinations: ", t)
