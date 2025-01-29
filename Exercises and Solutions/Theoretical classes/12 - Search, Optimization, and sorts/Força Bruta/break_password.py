import itertools
import random

p = [chr (i) for i in range (0,257)]

password = [random.choice (p), random.choice (p), random.choice (p)] 
 
print ("Password: ", password)

N = 3
for i in itertools.product (p, repeat = N):
    if list (i) == password:
        print ("Solution: ", str (i)) 
        break 


#print (p)