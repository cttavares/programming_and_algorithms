def extract_digit (n):
    return int (n % 10)

number = int (input ("Write number: "))
d1 = extract_digit (number)
number /= 10
d2= extract_digit (number)
number /= 10
d3 = extract_digit (number)
print ("Digits are: ", d1, d2, d3)
