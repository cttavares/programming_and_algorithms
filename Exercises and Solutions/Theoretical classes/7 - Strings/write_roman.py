n = 1994

def roman (n):
    if n > 1000:
        return "M" + roman (n - 1000)
    elif n >= 900 and n < 1000:
        return "CM"+ roman (n- 900) 
    elif n>=800:
        return "DCCC" + roman (n- 800)
    elif n>=700:
        return "DCC" + roman (n- 700)
    elif n>=600:
        return "DC"+roman (n-600)
    elif n>= 500:
        return "D"+roman (n-500)
    elif n>= 400:
        return "CD"+roman (n-400)
    elif n>= 300:
        return "CCC"+roman (n-300)
    elif n>= 200:
        return "CC"+roman (n-200)
    elif n>= 100:
        return "C"+roman (n-100)
    elif n>= 90:
        return "XC"+roman (n-90)
    elif n>= 80:
        return "LXXX"+roman (n-80)
    elif n>= 70:
        return "LXX"+roman (n-70)
    elif n>= 60:
        return "LX"+roman (n-60)
    elif n>= 50:
        return "L"+roman (n-50)
    elif n>= 40:
        return "XL"+roman (n-40)
    elif n>= 30:
        return "XXX"+roman (n-30)
    elif n>= 20:
        return "XX"+roman (n-20)
    elif n>= 10:
        return "X"+roman (n-10)
    elif n>= 9:
        return "IX"+roman (n-9)
    elif n>= 8:
        return "VIII"+roman (n-8)
    elif n>= 7:
        return "VII"+roman (n-7)
    elif n>= 6:
        return "VI"+roman (n-6)
    elif n>= 5:
        return "V"+roman (n-5)
    elif n>= 4:
        return "IV"+roman (n-4)
    elif n>= 3:
        return "III"+roman (n-3)
    elif n>= 2:
        return "II"+roman (n-2)
    elif n>= 1:
        return "I"+roman (n-1)
    else:
        return ""

print (roman (n))