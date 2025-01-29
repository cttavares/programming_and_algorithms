
from functools import reduce

s = {'bananas', 'peras', 'ananazes', 'pessegos', 'mangas'}

with open('fruits.txt', 'r') as file:
    r = [set (l) & s for l in [line.split() for line in file]]
    
    res = set ()
    for i in r:
        res |= i



print (res)