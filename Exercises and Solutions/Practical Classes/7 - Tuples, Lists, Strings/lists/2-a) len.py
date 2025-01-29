
def len_rec (l):
    if l == []:
        return 0
    else:
        return 1 + len_rec (l [1:])



l = [1,3,2,4,4,5,4]
print ("Len: ", len_rec (l))