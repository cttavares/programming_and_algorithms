def swap (x, y):
   return y, x

# To sort 4 numbers, 
# the bubble sort algorithm will be used
def sort_numbers(a, b, c, d):
    # Do a first round of comparisons
    # In order to fix d as the large number
    if a > b:
      (a, b) = swap (a, b)
    if (b > c):
       (b, c) = swap (b, c)
    if (c > d):
       (c, d) = swap (c, d)
    
    # Do a second round of comparisons
    # In order to fix c as the large number
    if a > b:
      (a, b) = swap (a, b)
    if b > c:
       (b, c) = swap (b, c)

    #
    if a > b:
       (a, b) = swap (a, b)
    
    return a, b, c, d

# Example
print(sort_numbers(4, 1, 3, 2))  # Outputs (1, 2, 3, 4)
