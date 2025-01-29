import random

number_is_right = False
numero_verdadeiro = random.randint (1, 50)
print ("Apagar: ", numero_verdadeiro)
tentativas = 0

while number_is_right == False:
    print ("Escreva a sua opção: ")
    print ("1. Adivinhar numero")
    print ("2. Desistir")
    opcao = int (input ("Opcao: "))
    if (opcao == 2):
        print ("Voce desistiu!")
        break
    else:
        numero = int (input ("Escreva numero: "))
        tentativas = tentativas + 1
        if numero == numero_verdadeiro:
            print ("Voce acertou! em ", tentativas)
            number_is_right = True
        elif numero < numero_verdadeiro:
            print ("O seu numero esta abaixo")
        else:
            print ("O seu numero esta acima")         
    