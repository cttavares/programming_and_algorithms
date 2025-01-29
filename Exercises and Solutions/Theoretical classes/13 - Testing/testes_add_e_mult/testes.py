from addiciona_e_multiplica import soma, multiplica

def testes_soma ():
    a = 1
    b = 2

    assert soma (a,b) == 3, "A funcao soma nao esta correcta"
    assert soma (0, 0) == 0, "A funcao soma nao esta correcta"


def testes_multiplica ():
    a = 2
    b = 2

    assert multiplica (a,b) == 4, "A funcao soma nao esta correcta"


testes_multiplica()
testes_soma ()