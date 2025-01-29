def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example
print(triangle_type(5, 5, 5))  # Outputs 'Equilateral'
