def reverse_number (n):
    reversed = 0
    potency = 0
    while n > 0:
        reversed = reversed * (10 ** potency)
        reversed += (n % 10) 
        n = n // 10

        if potency < 1:
            potency = 1
    
    return reversed

n = int (input ("Write n: "))
print ("Reversed is: ", reverse_number (n))
