t = "Isto e 66 texto. Nao 5 suposto dizer 3333 interessante"

for i in filter (lambda x: x!= "", map (lambda x: x if "ex" in x else "", t.split (" "))):
    print (i)


for i in filter (lambda x: x.startswith ("N"), t.split (" ")):
    print (i)