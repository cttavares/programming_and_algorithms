def brute_force_gcd (y, x):
    for i in range (y, 0, -1):
        if y % i == 0 and x % i == 0:
            return i

def gcd (y, x):
    while y != x:
        if y > x:
            y = y - x
        else:
            t = y
            y = x
            x = t
    
    return y 

def gcd_rec (y, x):
    if y > x:
        return gcd_rec (y-x, x)
    elif y == x:
        return y
    else:
        return gcd_rec (x, y)
    
min_gcd = gcd_rec (44, 12)
#min_gcd = gcd (44, 12)

#min_gcd = brute_force_gcd (15, 6)
print ("Min Gcd: ", min_gcd)