l = [i for i in range (1, 101)]
N = 10
set_map = {i % 10:set() for i in range (1, 11)}

for i in l:
     set_map [i % 10] = set_map [i % 10] | {i}

print (set_map)
