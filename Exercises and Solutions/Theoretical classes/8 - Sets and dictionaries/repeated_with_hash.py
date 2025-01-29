l = [9, 5, 4, 6, 7, 8, 8, 9, 7, 7, 1, 2, 3]
dict = {}

res = []
for i in l:
    if i not in dict: # Isto e tempo constante!
       dict [i] = "Batatas" 
       res.append (i)

print (res)