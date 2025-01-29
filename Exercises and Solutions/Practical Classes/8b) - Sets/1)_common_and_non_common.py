l = [12,13,14,14,15,16,16]
h = [12,13,14]

print ("common elements: ", set (l) & set (h))
print ("uncommon elements: ", (set (l) | set (h)) - (set (l) & set (h)))
print ("is subset", set (h).issubset (l) or  set (l).issubset (h))