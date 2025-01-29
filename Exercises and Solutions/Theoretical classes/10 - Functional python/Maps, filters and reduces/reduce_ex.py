from functools import reduce

def sum (a, b):
    return a+b

def square (a):
    return a * a

def cubic (a):
    return a * a * a

l = [i for i in range (1, 101)]


r2 = reduce(sum, map (square, l))
print ("Sum of squares: ", r2)

r3 = reduce (sum, map (cubic, l))
print ("Sum of cubes: ", r3)