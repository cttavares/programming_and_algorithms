import functools

l = [100 - i for i in range (0, 101)]

print ("Min: ", functools.reduce (lambda x,y: x if x < y else y, l))
print ("Max: ", functools.reduce (lambda x,y: x if x > y else y, l))