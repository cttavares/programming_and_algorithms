def show_table (n=-1):
    if n==-1:
        r = range (1, 10)
    else:
        r = range (n,n+1)

    for j in r:
        for i in range (1, 11):
            print (j, " x ", i, "= ", i*j)
    
n = int (input ("Write n (-1 for all):"))
show_table (n)