import random

posicao_x = 0 
n = 10

i = 0

print ("Posicao inicial: ", posicao_x)
while i < n:
    
    escolha = random.choice (['esquerda', 'direita'])
    if (escolha == 'esquerda'):
        print ("Vamos para a esquerda")
        posicao_x = posicao_x - 1
    else:
        posicao_x = posicao_x + 1
        print ("Vamos para a direita")
    
    print ("Posicao actual: ", posicao_x)
    i = i + 1
