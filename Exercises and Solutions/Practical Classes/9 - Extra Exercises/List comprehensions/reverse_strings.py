t = "algum texto sem sentido repetido so para ter mais palavras"

def reverse_string (s):
    r = list (s)
    r.reverse()
    return "".join (r)
    
print ([reverse_string (i) for i in t.split (" ")])