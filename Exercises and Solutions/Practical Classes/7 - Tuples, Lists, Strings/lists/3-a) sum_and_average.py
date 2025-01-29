l = []
for i in range (1, 101):
    l.append (i)

sum = 0
for i in l:
    sum += i

print ("sum of the list: ", sum, "; average: ", sum/len (l))
