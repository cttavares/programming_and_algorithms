l = []
for i in range (1, 101):
    l.append (101 - i)

l.sort ()
print ("L: ", l)

print ("Median: ", l [len (l)//2])