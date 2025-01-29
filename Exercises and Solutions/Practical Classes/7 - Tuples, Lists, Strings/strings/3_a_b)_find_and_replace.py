t = "Isto e 66 texto. Nao 5 suposto dizer 3333 interessante"

i = t.find("o")
while i != -1:
    print ("Found ", "o", " in ", i)
    i = t.find ("t", i+1)

v = t.replace("o", "a")
print ("Replaced: ", v)