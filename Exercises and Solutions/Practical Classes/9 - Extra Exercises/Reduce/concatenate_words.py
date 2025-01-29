import functools

t = "algum texto sem sentido repetido so para ter mais palavras"

# Concatenate strings with separator
print (functools.reduce (lambda x, y: x + "-" +y, t.split (" ")))

# Concatenate strings with condition
print (functools.reduce (lambda x, y: x + "- "+y, filter (lambda x: len (x) > 2, t.split (" "))))