
is_fruit = {'bananas', 'peras', 'ananazes', 'pessegos', 'mangas', 'morangos'}

with open('fruits.txt', 'r') as file:
          r = [set (line.split(" ")) & is_fruit for line in file]

c = set ()
for i in r:
    c = c | i 

print (c)