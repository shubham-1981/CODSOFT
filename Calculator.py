num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("\nSelect an operation to perform:")
print("+  for Addition")
print("-  for Subtraction")
print("*  for Multiplication")
print("/  for Division")
operation = input("Enter your choice: ")
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation! Please choose +, -, * or /")
