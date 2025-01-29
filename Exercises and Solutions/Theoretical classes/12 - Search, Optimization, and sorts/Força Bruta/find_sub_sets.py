import itertools
set_ = {1,2,3,4,5,6}

result = []
for j in range (0, len (set_)):
    for i in itertools.combinations (set_, j):
        result.append (set (i))

print (result)