l = [i for i in range (0, 10)]

def rotate_left (l):
    first = l [0]
    i = 0
    
    while (i < len (l)-1):
        l [i] = l [i+1]
        i = i + 1
    
    l [-1] = first

k = 3
for i in range (0, k):
    rotate_left (l)

print ("Rotated left: ", l)