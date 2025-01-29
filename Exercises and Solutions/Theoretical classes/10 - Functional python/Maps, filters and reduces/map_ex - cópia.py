def get_square_modulo_6 (s):
    return s % 6

l = [i for i in range (1, 101)]
#for i in l:
#    print (i)
 
lr = [i for i in map (get_square_modulo_6, l)]
#print ("Lista com map: ", lr)
lrr = [get_square_modulo_6 (i) for i in l]
if (lr == lrr):
    print ("Sao iguais")
#print (r [23]) 
#O r é "preguiçoso", mas é "iterável" 
#for i in r:
#    print (i)

#print ("----------")
#for i in r:
#    print (i)
