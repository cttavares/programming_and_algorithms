t = ("A", 12, (12, 13, 12))
print (t)
print (t [0], "-", t [2])

print ("B exists in tuple: ", "B" in t)
print ("A exists in tuple: ", "A" in t)

print ("12 exists ", t [2].count (12), " times.")

# An outlier is some element that is rare in comparison to others

t = (1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1)
print ("Element: ",t [0],";Frequency:",t.count (1)/len (t))
print ("Element: ",t [-3],";Frequency:",t.count (t [-3])/len (t))