import functools
import itertools

dice = [i for i in range (1, 7)]

k = 3
n = 2

def is_n6 (dice_rolls):
    count = 0
    for j in dice_rolls:
        if j == 6:
            count+= 1
    
    if count == n:
        print (dice_rolls)
        return 1
    else:
        return 0


count = functools.reduce (lambda x, y: x+y, map (is_n6, itertools.product (dice, repeat=k)))
print ("Number of sequences with ", count)