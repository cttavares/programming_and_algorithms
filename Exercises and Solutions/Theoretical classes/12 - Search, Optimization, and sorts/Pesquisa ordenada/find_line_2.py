import itertools

d = 5
points = []
points.append ((1, 1))
points.append ((2, 2))
points.append ((3, 3))
points.append ((0, 5))
points.append ((5, 5))
points.append ((6, 6))
points.append ((7, 7))
points.append ((8, 8))
points.append ((9, 9))


def distance (p1, p2):
    return (abs (p1 [0]-p2 [0])**2 + abs (p1[1]- p2 [1])**2)**0.5

def verify (i, d):
    if distance (i [0], i [1]) == d:
        return True
    else:
        return False

points.sort ()
for i in points:
    for j in points:
        if verify ((i, j), d) == True:
            print ("Soluttion:", i)
            break

        if d (i, j) > d:
            break     

for i in itertools.product (points, repeat = 2):
    print (i)
    
    

