year = 2025

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Ano e bissexto!")    
        else:
            print ("Ano nao e bissexto") 
    else:
        print ("Ano e bissexto!")
else:
    print ("Ano nao e bissexto!")

