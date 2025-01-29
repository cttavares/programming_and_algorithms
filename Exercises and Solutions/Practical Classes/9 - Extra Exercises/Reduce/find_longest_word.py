import functools 

t = "algum texto sem sentido repetido so para ter mais palavras"

print (functools.reduce (lambda x, y: x if len (x) > len (y) else y, t.split (" ")))