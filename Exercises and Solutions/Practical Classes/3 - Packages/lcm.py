import numpy as np

n = int(input("Enter the first number n: "))
m = int(input("Enter the second number m: "))
lcm = np.lcm(n, m)
print(f"Least common multiple: {lcm}")
