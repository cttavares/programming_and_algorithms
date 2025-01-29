class Proprietario:
    
    def __init__ (self, dinheiro, conta):
        self.dinheiro_bolso = dinheiro
        self.conta = conta
    
    def levantar (self, montante):
        return self.conta.levantar (montante)

class Gastador (Proprietario):
    def __init__ (self, dinheiro, conta):
        super().__init__ (dinheiro, conta)
        self.montante_a_retirar = 10
    
    def levantar(self, _):
        r = super().levantar (self.montante_a_retirar)
        #r = self.conta.levantar (self.montante_a_retirar)
        self.montante_a_retirar*=2
        return r

class Poupadinho (Proprietario):

    def __init__ (self, dinheiro, conta, montante_fixo):
        super().__init__ (dinheiro, conta)
        self.montante_fixo = montante_fixo        


    def levantar (self, _):
        return self.conta.levantar (self.montante_fixo)


class Conta:

    def __init__ (self, saldo_inicial, juro):
        self.saldo = saldo_inicial
        self.juro = juro

    def levantar (self, montante):
        if self.saldo >= montante:
            self.saldo -= montante

    def depositar (self, montante):
        self.saldo += montante

    def capitalizar (self):
        self.saldo*= (1+self.juro/100)

conta = Conta (1000, 1)
u1 = Poupadinho (20, conta, 10)
u2 = Gastador (0, conta)

print ("Dinheiro na conta", conta.saldo)
u1.levantar (10)
print ("Dinheiro na conta apos u1", conta.saldo)
u2.levantar (10)
print ("Dinheiro na conta", conta.saldo)
u2.levantar (10)
print ("Dinheiro na conta", conta.saldo)
