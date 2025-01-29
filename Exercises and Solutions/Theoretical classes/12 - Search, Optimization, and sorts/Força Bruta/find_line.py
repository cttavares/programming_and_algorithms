import itertools

d = 5
#points = []
#points.append ((1, 1))
#points.append ((2, 2))
#points.append ((3, 3))
#points.append ((0, 5))
#points.append ((5, 5))
#points.append ((6, 6))
#points.append ((7, 7))
#points.append ((8, 8))
#points.append ((9, 9))


points = [(i, i) for i in range (1, 10)]
points.append ((0, 5))

def distance (p1, p2):
    return (abs (p1 [0]-p2 [0])**2 + abs (p1[1]- p2 [1])**2)**0.5

def verify_solution (x1, x2):

    if (distance (x1, x2) == d):
        return True
    else:
        return False
    
def find_solution ():

    for i in itertools.combinations (points, 2):
        if verify_solution (i [0], i [1]) == True:
            return i

print ("A solucao da recta é: ", find_solution ())
