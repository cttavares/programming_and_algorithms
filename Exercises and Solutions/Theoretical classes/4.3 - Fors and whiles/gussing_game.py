import random

numero_computador = random.randint(0, 100)
tentativas = 1

utilizador_nao_venceu = True
utilizador_desistiu = False
print ("Numero gerado: ", numero_computador)
while utilizador_nao_venceu == True:
    numero_utilizador = int (input ("Escreva numero (-1 para desistir): "))
    if numero_utilizador == -1:
        print ("Voce desistiu!")
        break
    else:
        if numero_utilizador == numero_computador:
            print ("Voce ganhou em ",tentativas," tentativas! O numero: ", numero_computador)
            utilizador_nao_venceu = False
        elif numero_utilizador < numero_computador:
            print ("O numero esta acima, tente de novo!") 
        else:
            print ("O numero esta abaixo, tente de novo")  
    
    tentativas = tentativas + 1    
