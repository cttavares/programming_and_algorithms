# (id, nome, idade, prioridade)
lista_clientes = []
id = 0

def inserir_cliente ():
    global id
    id = id + 1 
    
    nome = input ("Escreva nome: ")
    idade = int (input ("Escreva idade: "))
    prioridade_t = (input ("Tem prioridade (s/n): "))

    prioridade = False
    if prioridade_t == "s":
        prioridade = True
    else:
        prioridade = False
    
    t = (id, nome, idade, prioridade)
    
    if (prioridade == False):
        lista_clientes.append (t)
    else:
        j = 0
        while j < len (lista_clientes) and lista_clientes [j][3] == True:
            j = j + 1
        
        lista_clientes.insert (j, t)
     
    
def mostrar_clientes ():
    for i in lista_clientes:
        print ("-------------")
        print ("Id: ", i [0])
        print ("Nome: ", i [1])
        print ("Idade: ", i [2])
        print ("Prioridade", i [3])
        print ("--------------------")

def remover_cliente ():
    id = int (input ("Escreva identificador a remover: "))
    for i in lista_clientes:
        if i [0] == id:
            lista_clientes.remove (i)  

opcao = 0
while (opcao != 4):
    print ("1. Inserir cliente")
    print ("2. Mostrar clientes")
    print ("3. Remover cliente")
    print ("4. Sair do programa")
    opcao = int (input ("Escreva a sua opcao: "))

    if (opcao == 1):
        inserir_cliente ()
    elif opcao == 2:
        mostrar_clientes ()
    elif opcao == 3:
        remover_cliente ()
