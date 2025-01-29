s = "123asasdsanasnd as231312ksakdkadkasdasdas!?!!!?"

num_caracters = len (s)
print ("Numero de caracteres", num_caracters)

count = 0 
for i in s:
    if (i.isalpha () == True):
        count += 1

    #count += i.isalpha ()

print ("Numero de caracteres alfa. ", count)

count = 0 
for i in s:
    if (i.isdigit() == True):
        count += 1

    #count += i.isalpha ()
print ("Numero de digitos: ", count)