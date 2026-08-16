# CODOMAX Internship - Module 2
# Project 1: Calculator
 
def calculator():
    print("=== Simple Calculator ===")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
 
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return
 
    print(f"Result: {num1} {op} {num2} = {result}")
 
 
if __name__ == "__main__":
    calculator()