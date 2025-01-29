def pop (position, l):
    e = l [position]
    return (e, l [0:position] + l [position+1:])

l = [1,3,2,4,4,5,4]
print ("Pop result ", pop (0, l))