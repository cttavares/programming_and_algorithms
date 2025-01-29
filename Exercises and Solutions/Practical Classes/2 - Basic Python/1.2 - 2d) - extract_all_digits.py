BASE = 2

def extract_digit (n):
    return int (n % BASE)

number = int (input ("Write number: "))
digits = []
while number > 0:
    d = extract_digit (number)
    digits.append (d)
    number //= BASE

print ("Digits: ", digits)

n = len (digits) - 1 
while n > 0:
    print (digits [n], ",")
    n = n - 1
print (", ", digits [0])