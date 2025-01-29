deck = [('2', 'S'), ('3', 'S'), ('4', 'S'), ('5', 'S'), ('6', 'S'), 
        ('7', 'S'), ('8', 'S'), ('9', 'S'), ('T', 'S'), ('J', 'S'),
        ('Q', 'S'), ('K', 'S'), ('A', 'S'), ('2', 'C'), ('3', 'C'),
        ('4', 'C'), ('5', 'C'), ('6', 'C'), ('7', 'C'), ('8', 'C'), 
        ('9', 'C'), ('T', 'C'), ('J', 'C'), ('Q', 'C'), ('K', 'C'), 
        ('A', 'C'), ('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H'), 
        ('6', 'H'), ('7', 'H'), ('8', 'H'), ('9', 'H'), ('T', 'H'), 
        ('J', 'H'), ('Q', 'H'), ('K', 'H'), ('A', 'H'), ('2', 'D'), 
        ('3', 'D'), ('4', 'D'), ('5', 'D'), ('6', 'D'), ('7', 'D'), 
        ('8', 'D'), ('9', 'D'), ('T', 'D'), ('J', 'D'), ('Q', 'D'), 
        ('K', 'D'), ('A', 'D')]

import itertools

all_solutions = []

def is_full_house (hand):
    cards = {}
    for i in hand:
        if i [0] not in cards:
            cards [i [0]] = 1
        else:
            cards [i [0]] += 1

    if len (cards) == 2:
        
        for i in cards.keys ():
            if cards [i] == 3 or cards [i] == 2:
                return True
        
    return False



for i in itertools.combinations (deck, 5):
    if is_full_house (i):
        all_solutions.append (i)

for i in all_solutions:
    print ("Full house: ", i)