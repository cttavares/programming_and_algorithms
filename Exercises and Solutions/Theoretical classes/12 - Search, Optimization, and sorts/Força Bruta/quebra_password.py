import itertools
#caracteres_possiveis = [chr (i) for i in range (0, 255)]

caracteres_possiveis = [chr (i) for i in range (65, 91)]
print ("Caracteres possiveis: ", caracteres_possiveis)

password = "AERO"

def is_verify (i):
    if i == password:
        return True
    else:
        return False

for i in itertools.product (caracteres_possiveis, repeat = 4):
    if is_verify ("".join (i)) == True:
        print ("A password é: ", i)
