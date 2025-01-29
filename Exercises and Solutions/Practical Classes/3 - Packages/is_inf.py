import numpy as np

def check_number(value):
    if np.isinf(value) and value > 0:
        return "Infinity"
    elif np.isinf(value) and value < 0:
        return "Negative Infinity"
    elif np.isnan(value):
        return "Not a Number"
    else:
        return "Neither"

value = float(input("Enter a number: "))
print(check_number(value))
