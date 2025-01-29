import functools

t = "Isto e 66 texto. Nao 5 suposto dizer 3333 interessante"
for i in map (lambda x: (x, len (x)), t.split (" ")):
    print (i)

#r = functools.reduce (lambda x, y: len (x [0]), map (lambda x: (x, len (x)), t.split (" ")))
largest = functools.reduce (lambda x, y: x if (len (x [0]) > len (y [0])) else y, map (lambda x: (x, len (x)), t.split (" ")))
smallest = functools.reduce (lambda x, y: x if (len (x [0]) < len (y [0])) else y, map (lambda x: (x, len (x)), t.split (" ")))

print ("Largest: ", largest, "; smallest: ", smallest)