import itertools
dict = {"Lisboa": dict (), "Braga": dict (), "Guimaraes": dict (), "Vila Nova de Gaia": dict ()}

dict ["Lisboa"] = {"Guimaraes":20, "Braga":20, "Vila Nova de Gaia":10, "Lisboa":0}
dict ["Braga"] = {"Guimaraes":500, "Braga":0, "Vila Nova de Gaia":10, "Lisboa":20}
dict ["Guimaraes"] = {"Guimaraes":0, "Braga":1000, "Vila Nova de Gaia":10, "Lisboa":20}
dict ["Vila Nova de Gaia"] = {"Guimaraes":10, "Braga":10, "Vila Nova de Gaia":0, "Lisboa":10}


def score (solucao):
    custo_total = 0
    index = 0
    while index < len (solucao)-1:
        cidade_actual = solucao [index]
        cidade_a_viajar = solucao [index+1]
        custo_total += dict [cidade_actual][cidade_a_viajar]
        index = index + 1
    
    return custo_total

score_min = -1
solucao = tuple ()

for i in itertools.permutations (dict):
    if score_min == -1:
        score_min = score (i)
        solucao = i
    else:
        s_temp = score (i)
        if s_temp <= score_min:
            score_min = s_temp
            solucao = i
    
print ("A melhor solucao é: ", solucao)