def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/' and num2 != 0:
        return num1 / num2
    elif operation == '/' and num2 == 0:
        return 'Error: Division by zero'
    else:
        return 'Invalid operation'

# Example
print(calculator(5, 3, '+'))  # Outputs 8
