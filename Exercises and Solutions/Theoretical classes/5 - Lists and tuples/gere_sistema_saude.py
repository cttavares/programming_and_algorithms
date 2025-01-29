# Client tem o tipo tuplo (texto, int, {True, False})

lista_clients = []

def inserir_cliente ():
    nome = input ("Escreva o nome: ")
    idade = int (input ("Escreva a idade: "))
    prioridade_t = input ("Escreva prioridade (y/n): ")
    prioridade = False
    
    if prioridade_t == "y":
        prioridade = True
    
    if lista_clients == []:
        lista_clients.append ((nome, idade, prioridade))
    else:
        if prioridade == False:
            lista_clients.append ((nome, idade, prioridade))
        else:
            local_insercao = 0
            while local_insercao < len (lista_clients) and lista_clients [local_insercao][2] == True:
                local_insercao = local_insercao + 1
            
            if local_insercao < len (lista_clients):    
                lista_clients.insert(local_insercao, (nome, idade, prioridade))
            else:
                lista_clients.append ((nome, idade, prioridade))



def ver_lista_clients ():
    print ("List de clientes *************")
    print (lista_clients)

def remover_clientes ():
    nome = input ("Escreva nome a remover: ")
    for i in lista_clients:
        if i [0] == nome:
            lista_clients.remove (i)
            break 

opcao = -1
# opcao 4 para sair
while (opcao != 4):
    print ("1- Inserir cliente")
    print ("2- Ver lista clientes")
    print ("3 - Remover client")
    print ("4 - Sair")
    opcao = int (input ("O que fazer?: "))

    if opcao == 1:
        inserir_cliente ()
    elif opcao == 2:
        ver_lista_clients ()
    elif opcao == 3:
        remover_clientes ()
