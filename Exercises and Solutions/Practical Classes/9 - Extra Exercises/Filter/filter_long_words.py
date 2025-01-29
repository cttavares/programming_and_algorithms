t = "algum texto sem sentido repetido so para ter mais palavras"

print ([i for i in filter (lambda x: len(x) > 5, t.split (" "))])