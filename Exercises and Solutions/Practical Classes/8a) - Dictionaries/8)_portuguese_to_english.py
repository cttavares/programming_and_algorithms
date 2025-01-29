portuguese_to_english = {"casa": "house", 
                         "gato": "cat", 
                         "cachorro": "dog", 
                         "banana" : "banana" , 
                         "amigo": "friend", 
                         "livro": "book",
                         "computador" : "computer",
                         "sol": "sun", 
                         "lua": "moon"}

frase = "eu tenho um cachorro e um gato amigo em casa, gosto de lhe atirar com um livro e com uma banana. \n O gato gosta do sol e da lua e de atirar o computador ao chao"
print (frase)

translated_frase = frase

for i in frase.split (" "):
    if i in portuguese_to_english:
        translated_frase = translated_frase.replace (i, portuguese_to_english [i])

print ("translated: ", translated_frase)