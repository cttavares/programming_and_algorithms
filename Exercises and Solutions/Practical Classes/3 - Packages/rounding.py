import numpy as np

number = float(input("Enter the number: "))
decimals = int(input("Enter the number of decimals: "))
rounded = np.round(number, decimals)
print(f"Rounded:", rounded)
