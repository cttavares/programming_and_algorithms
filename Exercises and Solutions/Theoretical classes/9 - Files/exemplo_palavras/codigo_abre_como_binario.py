with open ("exemplo_palavras/palavras_repetidas.csv", "rb") as f:
    a = f.read ()

count = 0
limit = 20

for i in a:
    if (count >= limit):
        count = 0
        print ("")
    
    print (hex (i), end =" ")
    count = count + 1
        