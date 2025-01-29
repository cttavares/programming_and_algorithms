l = []
for i in range (1, 11):
    l.append (i)

i = 0
while i < len (l)//2:
    temp = l [i]
    l [i] = l [len (l)-i - 1]
    l [len (l)-i - 1] = temp
    i = i + 1

print ("Reversed list: ", l)