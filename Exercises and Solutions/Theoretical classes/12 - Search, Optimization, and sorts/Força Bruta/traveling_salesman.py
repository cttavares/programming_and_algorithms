import itertools
dict = {"Lisboa": [], "Braga": [], "Guimaraes": [], "Vila Nova de Gaia": []}

dict ["Lisboa"] = [0, 20, 20, 10]
dict ["Guimaraes"] = [20, 0, 1000, 10]
dict ["Braga"] = [20, 500, 0, 10]
dict ["Vila Nova de Gaia"] = [10, 10, 10, 0]

solucao = ["Lisboa", "Guimaraes", "Braga", "Vila Nova de Gaia"]

def get_index (city):
    if city == "Lisboa":
        return 0
    elif city == "Guimaraes":
        return 1
    elif city == "Braga":
        return 2
    else: 
        return 3

def score_ (partida, destino):
    print ("Custo: ", partida," a ", destino, "e ", dict [partida][get_index (destino)])
    return dict [partida][get_index (destino)]

def score (solucao):
    print ("-------")
    score = 0
    score += score_ (solucao [0], solucao [1])
    score += score_ (solucao [1], solucao [2])
    score += score_ (solucao [2], solucao [3])
    print ("-------")
    return score

maximum_score = 100000
for i in itertools.permutations (solucao):
    if score (i) < maximum_score:
        maximum_score = score (i)
        best_solution = i

print ("Best solution", best_solution)