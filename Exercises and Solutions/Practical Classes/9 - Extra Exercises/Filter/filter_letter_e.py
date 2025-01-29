t = "algum texto sem sentido repetido so para ter mais palavras"

print ([i for i in filter (lambda x: not ("e" in x), t.split (" "))])