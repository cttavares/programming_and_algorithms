t = "r over z over h over"

r = t.split (" ")

p = "over"

count = 0
for i in r:
    if i == p:
        count = count + 1

print ("Instancias: ", count)