import random 

N = 1000
dict = list ()
for i in range (0,N):
    dict.append ([])

def hash (name): 
    hash = 0
    #for i in name: 
    #    hash -= ord (i) 
    hash = int (name)
    return hash % N

def save (key, value):
    if (key, value) not in dict[hash (key)]:
        dict [hash (key)].append ((key, value))

def retrieve (key):
    for i in dict (hash (key)):
        if i [0] == key:
            return i 

Random_numbs = 1000
for i in range (0, Random_numbs):
    n = random.randint(0, 100)
    save (str (n), str (n))

num_empty = 0
collisions = 0
for i in dict:
    
    if i != []:
        collisions += len (i) - 1

        print_s = ""
        for j in i:
            print_s += "->" + str(j)
        print (print_s)
    else:
        num_empty = num_empty + 1

print ("Empties: ", num_empty)
print ("Collions: ", collisions)
print ("Collisin average: ", collisions/(N-num_empty))
