N = 5
t = [["L" for _ in range (N)] for _ in range (N)]

t [2][1] = "P"
t [2][2] = "P"

for x, i in enumerate (t):
    for y, j in enumerate (i):
        print (t [x][y], end = " ")
    print ("")

def flood (x, y, visited):

    if x >= N or x < 0 or y >= N or y < 0:
        return
    elif (x,y) in visited:
        return
    elif t [x][y] != "L":
        return 
    else:
        visited.add ((x,y))
         
        flood (x+1, y, visited)
        flood (x-1, y, visited)
        flood (x, y+1, visited)
        flood (x, y-1, visited)

        return 

def flood_ (x,y, visited):
    if x >= N or x < 0 or y >= N or y < 0:
        return
    elif (x,y) in visited:
        return 
    elif t [x][y] != "L":
        return
    else:   
        visited.add ((x,y))
        # Para baixo
        flood_ (x, y+1, visited)
        # Para cima
        flood_ (x, y-1, visited)
        # Para a esquerda
        flood_ (x-1, y, visited)
        # Para a direita
        flood_ (x+1, y, visited)
        
        return 

#s = set ()
#flood_ (0, 0, s)
#print ("Pontos visitados:", s)


# Conjunto intento
whole_set = set ()
for x in range (N):
    for y in range (N):
        whole_set.add ((x,y))

print (whole_set)

disjoint = []
while whole_set != set ():
     elem = [i for i in whole_set][0]
     result = set ()
     flood (elem [0], elem [1], result)
     print ("Result: ", result)
     disjoint.append (result)

     whole_set = whole_set - result
     print ("Whole set -:", whole_set - result)

print ("Disjoint: ",disjoint)
