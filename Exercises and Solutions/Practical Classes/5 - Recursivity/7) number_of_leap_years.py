# Uma funcao simples que verifica se um ano e bissexto
def e_bissexto (year):
    return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)

# Uma funcao recursiva de contagem de anos bissextos 
# num dado intervalo
def conta_anos_bissextos (i, f):
    if i > f:
        return 0
    else:
        return e_bissexto (i) + conta_anos_bissextos (i+1, f)

print ("Anos bissextos: ", conta_anos_bissextos (2000, 2020))