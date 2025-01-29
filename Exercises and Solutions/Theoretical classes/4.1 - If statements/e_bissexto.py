ano = 2000

if ((ano % 4 == 0 and not (ano % 100 == 0)) or (ano % 400 == 0)):
    print ("O ano e bissexto")
else:
    print ("O ano nao e bissexto")