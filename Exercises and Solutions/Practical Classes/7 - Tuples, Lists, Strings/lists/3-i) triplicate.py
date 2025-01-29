l = [1,2,2, 3,4,5,6,7,7,7,8,9]

i = 0
while i < len (l):
    if l.count (l [i]) > 1:
        for j in range (0,2):
            l.insert (i, l [i])
        i = i + 2
    
    i = i + 1

print ("Nova lista: ", l)