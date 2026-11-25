"""
Question 1 — Advanced Arithmetic Calculator
Problem statement
Write a Python program that accepts two numbers and performs all seven arithmetic operations.
Requirements
Accept two numeric inputs.
Calculate addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
Handle division-by-zero errors.
Display results using f-strings.
Include meaningful comments.
"""

# Accepting two num from user 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero for division, floor division, and modulus
try:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
except ZeroDivisionError:
    division = "Undefined (division by zero)"
    floor_division = "Undefined (division by zero)"
    modulus = "Undefined (division by zero)"

# Exponentiation
exponentiation = num1 ** num2

print("============ARITHMETIC OPERATIONS RESULTS ============")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
print("========================================")


