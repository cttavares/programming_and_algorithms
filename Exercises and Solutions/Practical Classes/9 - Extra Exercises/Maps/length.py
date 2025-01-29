t = "algum texto sem sentido repetido so para ter mais palavras"

for i in map (lambda x: len (x), t.split (" ")):
    print (i)