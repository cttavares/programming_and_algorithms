import numpy as np

n = int(input("Enter the first number n: "))
m = int(input("Enter the second number m: "))
gcd = np.gcd(n, m)
print(f"Greatest common divisor: {gcd}")
