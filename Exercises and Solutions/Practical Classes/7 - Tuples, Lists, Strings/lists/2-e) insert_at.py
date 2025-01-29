def insert_at (index, element, list):
    return list [0:index] + [element] + list [index+1:]

l = [1,3,2,4,4,5,4]
print ("insert_at: ", insert_at (0, 6, l))
print ("insert_at: ", insert_at (547, 6, l))