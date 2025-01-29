import random


def cifrar (mensagem, chave):
    m_d = list (mensagem)
    m_c = []
    for i in m_d:
        m_c.append (chave [ord (i) - 65])
    return "".join (m_c) 

def get_posicao (chave, to_find):
    for index, i in enumerate (chave):
        if to_find == i:
            return index

def decifrar (mensagem, chave):
    m_c = list (mensagem)
    m_d = []

    for i in m_c:
        m_d.append (chr (get_posicao (chave, i)+65))
    
    return "".join (m_d)


#chave = [chr (i) for i in random.sample (range (65, 91), 26)]
chave = ['P', 'J', 'X', 'Y', 'V', 'D', 'E', 'G', 'O', 'S', 'B', 'U', 'A', 'T', 'R', 'I', 'W', 'F', 'L', 'C', 'M', 'K', 'Q', 'H', 'N', 'Z']
print ("Lista de cifra: ", chave)

mensagem_plana = "ABZ"
resultado = cifrar (mensagem_plana, chave)
print ("Mensagem cifrada", resultado)

resultado_decifra = decifrar (resultado, chave)
print ("Mensagem decifrada", resultado_decifra)

