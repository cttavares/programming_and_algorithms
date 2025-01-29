import random

l = [random.randint (0, 20) for _ in range (0,10)]

def swap (l, i, j):
    t = l [i]
    l [i] = l [j]
    l [j] = t
    return l

def bubble_sort (l):
    n = len (l)-1
    for j in range (n, 0, -1):  
        for i in range (0, j):
            if l [i] > l [i+1]:
                swap (l, i, i+1)

print ("Original: ", l)
bubble_sort (l)
print ("Sorted: ", l)