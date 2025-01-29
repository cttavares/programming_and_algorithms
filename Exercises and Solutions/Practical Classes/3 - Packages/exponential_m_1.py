import numpy as np

number = float(input("Enter the number: "))
exp_minus1 = np.expm1(number)
print(f"Exponential minus 1: {exp_minus1}")
