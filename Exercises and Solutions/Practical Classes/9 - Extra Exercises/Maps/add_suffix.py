t = "algum texto sem sentido repetido so para ter mais palavras"
suffix = "(peta)"

for i in map (lambda x: x+suffix, t.split (" ")):
    print (i)    