l1 = [i for i in range (5, 16)]
l2 = [i for i in range (12, 36)]
inter = []

for i in l1:
    if i in l2:
        inter.append (i)

print ("Common: ", inter)