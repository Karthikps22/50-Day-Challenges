# 🧮 Simple Calculator for Two Numbers

print("🔢 Welcome to the Simple Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operation == '+':
    result = num1 + num2
    print(f"✅ {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"✅ {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"✅ {num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"✅ {num1} / {num2} = {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
else:
    print("❌ Invalid operation. Please choose from +, -, *, /.")
