# Mini Calculator
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Choose operation (add/sub/mult/div): ")
if operation == "add":
    print("Result:", a + b)
elif operation == "sub":
    print("Result:", a - b)
elif operation == "mult":
    print("Result:", a * b)
elif operation == "div":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation selected!")
