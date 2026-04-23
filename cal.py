def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return 
        return a / b
    else:
        return 

# Example
print(calculator(10, 5, '+'))  # 15