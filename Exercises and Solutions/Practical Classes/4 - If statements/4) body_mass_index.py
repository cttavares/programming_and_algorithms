def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if 18.5 <= bmi <= 24.9:
        return bmi, "Healthy"
    elif 25 <= bmi <= 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"

# Example
print(calculate_bmi(70, 1.75))  # Outputs BMI and health conclusion
