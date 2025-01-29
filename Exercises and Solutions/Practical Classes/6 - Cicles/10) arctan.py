from numpy import rad2deg, arctan

def prod (x, n):
    prod = 1
    for k in range (1, n+1):
        prod*= (2*k*x**2)/((2*k+1)*(1+x**2))
    return prod

def arctan_ (x, max):
    result = 0 
    for n in range (0, max):
        result = result + prod (x, n)
    return (x/(1+x**2))*result

x = float (input ("Write an x: "))
max = int (input ("Write the number of elements in the series: "))
r = arctan_ (x, max)
z = arctan (x)
print ("The arctan of ", x, " is (in degrees): ", rad2deg (r), "Error margin: ", (abs (rad2deg (z)- rad2deg (r))))