def numeric_to_roman (n):
    pre = ""
    r = 0
    if n >= 1000:
        pre = "M"
        r = 1000
    elif n >= 900:
        pre = "CM"
        r = 900
    elif n >= 500:
        pre = "D"
        r = 500
    elif n >= 400:
        pre = "CD"
        r = 400
    elif n >= 100:
        pre = "C"
        r = 100
    elif n >= 90:
        pre = "XC"
        r = 90
    elif n >= 50:
        pre = "L"
        r = 50
    elif n >= 40:
        pre = "XL"
        r = 40
    elif n >= 10:
        pre = "X"
        r = 10
    elif n >= 9:
        pre = "IX"
        r = 9
    elif n >= 5:
        pre = "V"
        r = 5
    elif n >= 4:
        pre = "IV"
        r = 4
    elif n >= 1:
        pre = "I"
        r = 1
    else:
        return ""
    
    return pre + numeric_to_roman (n - r)

n = int (input ("Write a number: "))
print ("The translation is ", numeric_to_roman (n))