texto = "- Um primeiro-ministro diz ao país que aceitou o pedido de demissão de secretários de Estado para estes poderem solicitar ser constituídos arguidos e depois descobre-se que, afinal, resignaram porque já tinham percebido que iriam, de qualquer modo, ser constituídos arguidos;"
texto = texto.replace ("-"," ")
texto = texto.replace (",","")
texto = texto.replace (";","")
texto = texto.strip(" ")
print (texto)

freq = dict ()
for i in texto.split (" "):
    if i in freq:
        freq [i] += 1
    else:
        freq [i] = 1
    
print ("Freqs: ", freq)
