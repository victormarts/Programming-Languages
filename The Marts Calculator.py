
# NAME: VICTOR MARTIN ODUOR ONYANGO REG: SCT211-0096/2022

# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "We don't do that on earth! Division by zero is not allowed"
    return x / y

# Welcome Note
print("Welcome to The Marts Calculator. To exit the calculator, enter 'X' at any prompt.")

# Input Starts here
while True:
    try:
        num1 = input("Enter the first number (integer or float): ")

        # Allow the user to exit by pressing 'X'
        if num1 == 'X' or num1 == 'x':
            break

        num1 = float(num1)

        num2 = float(input("Enter the second number (integer or float): "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == 'X' or operator == 'x':
            break

        while operator not in ('+', '-', '*', '/'):
            print("Wrong operator. Please enter a valid operator (+, -, *, /)")
            operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")

    except ValueError:
        print("Invalid value. Please enter valid numeric values.")
