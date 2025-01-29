import os 
import time

labirinto = [
    ["🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳"],
    ["🌳", "  ", "  ", "🚧", " ", "🌴", "  ", "🚧", "  ", "🌳"],
    ["🌳", "  ", "🌴", "🚧", " ", "🌳", "  ", "🚧", "  ", "🌳"],
    ["🌳", "  ", "  ", " ", "  ", "  ", "  ", "🚧", "  ", "🌳"],
    ["🌳", " ", "🌲", "  ", "🌳", "🚧", "  ", "  ", "  ", "🌳"],
    ["🌳", "  ", "🧱", "  ", "🌳", "  ", "🚧", "🚧", "💎", "🌳"],
    ["🌳", "  ", "🌳", " ", " ", "  ", "💧", "  ", "  ", "🌳"],
    ["🌳", "  ", "🌲", "  ", " ", "🌴", "🚧", "  ", "🚧", "🌳"],
    ["🌳", "  ", "  ", "  ", "🧱", "🚧"," ", "  ", "🌳", "🌳"],
    ["🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳", "🌳"],
]

hero = (1, 1, "🚶", "  ")

def actualiza_posicao_heroi (x, y):
    global hero
    labirinto [hero [0]][hero [1]] = hero [3]
    hero = (x, y, "🚶", labirinto [x][y])
    labirinto [hero [0]][hero [1]] = hero [2]

def mostra_labirinto ():
    for linha in range (len (labirinto)):
        for coluna in range (len (labirinto [linha])):
            print (labirinto [linha][coluna], " ", end = "")
        print ("")

def mostra_alterando_consola():
    print("\033[0;0H"*(len (labirinto)-1), end = "")
    print ("\n") 
    mostra_labirinto ()
    
def resolve_com_backtrack (x, y, ja_visitadas = set ()):
    if (x, y) in ja_visitadas:
        return False

    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return False
    
    if labirinto [x][y] == "💎":
        print ("Encontrou o tesouro!")
        return True

    if labirinto [x][y] == " " or labirinto [x][y] == "  ":
        refresh(x, y)

        ja_visitadas.add ((x,y))
        
        if resolve_com_backtrack (x-1, y, ja_visitadas) == True:
            return True
        refresh (x,y)
        if resolve_com_backtrack (x+1, y, ja_visitadas) == True: 
            return True
        refresh (x,y)
        if resolve_com_backtrack (x, y+1, ja_visitadas) == True:
            return True
        refresh (x,y)
        if resolve_com_backtrack (x, y-1, ja_visitadas) == True:
            return True
        
        refresh (x,y)
    else:
        return False

def refresh(x, y):
    actualiza_posicao_heroi (x, y)
    mostra_alterando_consola ()
    time.sleep (1)


os.system('cls' if os.name == 'nt' else 'clear')
mostra_alterando_consola ()
#time.sleep (1)
#actualiza_posicao_heroi (1,1)
#mostra_alterando_consola ()
#time.sleep (1)
#actualiza_posicao_heroi (2,1)
#mostra_alterando_consola ()
if resolve_com_backtrack (1,1) == False:
    print ("Não encontrou o tesouro!")