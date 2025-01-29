l = [9, 5, 4, 6, 7, 8, 1, 2, 3]

# First solution using sorting (N log N)
#l.sort ()
#print ("Minimum: ", l [0])
#--------------------------------


# Second solution using a while (N)
#minimum = l [0]
#for i in l:
#    if i < minimum:
#        minimum = i
# -----------------------------

# Third solution using a while (N)
i = 0
minimum = l [0]

while i < len (l):
    if l [i] < minimum:
        minimum = l [i]
    i = i + 1
#---------------------------
print ("Minimum: ", minimum)