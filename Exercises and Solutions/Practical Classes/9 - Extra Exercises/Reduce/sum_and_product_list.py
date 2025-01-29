import functools

# Sum of the elements in a list
print (functools.reduce (lambda x, y: x+y, range (1, 101)))

# Product of the elements in a list
print (functools.reduce (lambda x, y: x*y, range (1, 101)))
