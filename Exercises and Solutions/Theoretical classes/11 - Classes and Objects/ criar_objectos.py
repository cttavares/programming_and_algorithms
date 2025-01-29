class vazio:
    pass

objecto = vazio ()

print (objecto)
print (type (objecto))

class personagem_ficticia:
    name = ""
    idade = 120

p = personagem_ficticia ()
print ("Personagem ficticia, Nome: ", p.name, "Idade: ", p.idade)
p.name = "Tartaruga Genial"
print ("Personagem ficticia, Nome: ", p.name, "Idade: ", p.idade)

class personagem_ficticia_com_construtor ():

    def __init__ (self, name="Vegeta", idade=100):
        self.name = name
        self.idade = idade

c = personagem_ficticia_com_construtor ()
print ("Personagem ficticia com construtor, Nome: ", c.name, "Idade: ", c.idade)

d = personagem_ficticia_com_construtor ("Son Go ku", 50)
print ("Personagem ficticia com construtor, Nome: ", d.name, "Idade: ", d.idade)

d.name = "Son go Ten"
d.idade = 123
print ("Personagem ficticia com construtor, Nome: ", d.name, "Idade: ", d.idade)