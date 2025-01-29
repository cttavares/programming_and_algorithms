with open ("palavras_repetidas.csv", "r") as f:
    s = f.readlines ()

frequencia_palavras = dict ()

for i in s:
    palavras = i.split ()
    for j in palavras:
        if j not in frequencia_palavras:
            frequencia_palavras [j] = 1
        else:
            frequencia_palavras [j] += 1

print ("Frequencia palavras: ", frequencia_palavras)

#print (s)

palavras_alegres = ["escola", "livro", "caneta", "praxe"]
palavras_tristes = ["programa", "código"]

palavras_alegres_count = 0
palavras_tristes_count = 0

for i in frequencia_palavras:
    if i in palavras_alegres:
        palavras_alegres_count = palavras_alegres_count + 1
    
    if i in palavras_tristes:
        palavras_tristes_count = palavras_alegres_count + 1

if palavras_alegres_count > palavras_tristes_count:
    print ("O texto é alegre!")
else:
    print ("O texto é triste")