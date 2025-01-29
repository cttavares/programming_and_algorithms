l = [i for i in range (0, 10)]

element = 4
pivot_position = -1

r = ([], [])

for index, v in enumerate (l):
    if v == element:
        r = (l [:index], l [index+1:])

print ("Pivoted result: ", r)