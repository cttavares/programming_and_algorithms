n = 10
var_minus_1 = 1 
var_minus_2 = 1
for i in range (2, n+1):
    print ("var_1 ", var_minus_1, ";var_2:", var_minus_2)
    current = var_minus_2 + var_minus_1 
    var_minus_1 = var_minus_2 
    var_minus_2 = current

print ("Nth value", var_minus_2)