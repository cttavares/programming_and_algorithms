str = "abbabababababbabbaba"

lt = []
lt.append ((2, 2, 4))
lt.append ((3, 0, -1))
lt.append ((4, 5, 5))

nov = ""
for i in lt:
    (copies, low, high) = i
    subs = str [low:high]
    subs = subs * copies
    nov = str [0:low] + subs + str [high:-1]
    str = nov

print (str)