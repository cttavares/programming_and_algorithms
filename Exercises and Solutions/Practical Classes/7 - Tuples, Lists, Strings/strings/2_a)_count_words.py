import functools

t = "Isto e um texto. Nao e suposto dizer nada interessante"

spl = t.split (" ")
print ("Numbero de palavaras: ", len (spl))

word_freq = dict ()

for i in spl:
    if i in word_freq:
        word_freq [i] += 1
    else:
        word_freq [i] = 1

print ("Word freq: ", word_freq)

max = ("", 0)
for i in word_freq:
    if word_freq [i] > max [1]:
        max = (i, word_freq [i])

min = max
for i in word_freq:
    if word_freq [i] < min [1]:
        min = (i, word_freq [i])

print ("Max: ", max)
print ("Min", min)


