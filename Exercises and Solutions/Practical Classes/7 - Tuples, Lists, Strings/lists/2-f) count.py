def count (element, l):
    count = 0
    for i in l:
        if i == element:
            count = count + 1
    
    return count

def count_rec (element, l):
    if l == []:
        return 0
    else:
        return (l [0] == element) + count_rec (element,l [1:])
    
l = [1,3,2,4,4,5,4]
print ("Count: ", count_rec (4, l))