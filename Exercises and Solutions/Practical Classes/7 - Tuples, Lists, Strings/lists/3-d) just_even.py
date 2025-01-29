l = []
for i in range (1, 11):
    l.append (i)

n = []
for i in l:
    if i % 2 == 0:
        n.append (i)


print ("Old list: ", l)
print ("New list: ", n)