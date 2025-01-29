import functools

t = "Isto e 66 texto. Nao 5 suposto dizer 3333 interessante"

def is_not_only_numbers (s):
    for i in s:
        if not i.isdigit():
            return 1

    return 0

sum = functools.reduce (lambda x,y: x+y, map (is_not_only_numbers, [i for i in t.split ()]))
print ("Not only numbers is: ", sum)