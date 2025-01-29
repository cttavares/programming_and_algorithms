def extract_second_digit(n):
    digito_2 = n // 10 + 1
    return digito_2

def extract_first_digit(n):
    digito_1 = n % 10 * 4
    return digito_1


def recebe_number (n):
    assert n >= 20 and n <=40, "O seu numero nao esta entre 20 e 40"
    digito_1 = extract_first_digit(n)
    digito_2 = extract_second_digit(n)
    assert digito_1 == (n %10), "Algo correu mal"
    assert digito_2 == (n // 10), "Algo correu mal"
        
    
    
    digito_1 += 1945
    digito_2 += 1945

    digito_1*=46**2
    digito_2*=46**2

    r = (digito_2 + digito_1) % 349
    r //=10
    return r


print ("O resultado disto é", recebe_number (35))