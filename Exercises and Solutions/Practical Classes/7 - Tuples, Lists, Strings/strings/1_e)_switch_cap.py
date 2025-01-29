s = "ABSDabsshahdbq17231absA"

i = 0

f = ""
while i < len (s):
    if s[i].islower():
       f+= s [i].upper()
    else:
       f+= s [i].lower()  
    
    i = i + 1 

print ("F: ", f)