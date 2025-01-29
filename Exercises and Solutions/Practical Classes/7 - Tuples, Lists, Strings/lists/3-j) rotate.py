l = [i for i in range (0, 10)]

def rotate_right (l):
    last = l [-1]
    i = len (l)-1
    while (i >= 1):
        l [i] = l [i-1]
        i = i - 1
    l [0] = last

rotate_right (l)
print ("New list: ", l)
