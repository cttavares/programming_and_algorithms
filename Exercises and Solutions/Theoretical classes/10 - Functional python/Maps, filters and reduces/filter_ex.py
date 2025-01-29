def exclude_uneven (s): 
    if s % 2 == 0:
        return True 
    return False

def exclude_not_prefix (s): 
    return not (s.startswith ("ABBA"))

words = ["ABBAJOUR", "BBBBC", "ABBATE", "ABBACATE", "CACT"]

f = filter (exclude_not_prefix, words)
fl = [i for i in f]
print (fl)


#l = [i for i in range (1, 11)]
#r = filter (exclude_uneven, l)
#e = [i for i in r]




