def is_not_odd (a):
    return a % 2 == 0

#r = filter (is_not_odd, range (1, 101))
#for i in r:
#    print (i)

#print ("-------")
c = [i for i in range (1, 101) if is_not_odd (i)]

d = [i for i in range (1, 101) if is_not_odd (i)] 
for j in d:
    print (j)