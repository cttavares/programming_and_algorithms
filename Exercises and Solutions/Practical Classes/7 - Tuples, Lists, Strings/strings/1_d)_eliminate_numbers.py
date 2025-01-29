s = "a1231asdasabfdsa34546532"

f = ""
for i in s:
    if not i.isdigit():
        f+= i

print ("F: ", f)
