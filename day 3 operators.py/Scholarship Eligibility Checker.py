"""
Question 2 — Scholarship Eligibility Checker
Problem statement
Develop a Python program that determines whether a student is eligible for a scholarship based on academic performance, attendance, and family income.
Eligibility criteria
A student is eligible only when all three conditions are satisfied:
The percentage is at least 80%.
Attendance is at least 75%.
Annual family income is ₹3,00,000 or less.
Use comparison and logical operators to determine eligibility. Validate percentage and attendance between 0 and 100, and reject negative income.
"""
name = input("Enter your name: ")
percentage = input("Enter your marks percentage: ")
attendance = input("Enter your attendance percentage: ")
family_income = input("Enter your annual family income (in ₹): ")

# Validate percentage and attendance
if not percentage.replace('.', '', 1).isdigit() or not attendance.replace('.', '', 1).isdigit():
    print("Invalid input. Please enter valid numbers for percentage and attendance.")
    exit()

# Validate family income
if not family_income.replace('.', '', 1).isdigit():
    print("Invalid input. Please enter a valid number for family income.")
    exit()
# Convert inputs to appropriate data types
percentage = float(percentage)
attendance = float(attendance)
family_income = float(family_income)

# Validate ranges
if not (0 <= percentage <= 100) or not (0 <= attendance <= 100):
    print("Invalid input. Please enter values for percentage and attendance between 0 and 100.")
    exit()

if family_income < 0:
    print("Invalid input. Please enter a valid family income.")
    exit()

# Check eligibility criteria
if percentage >= 80 and attendance >= 75 and family_income <= 300000:
    print(f"Congratulations, {name}! You are eligible for the scholarship.")
else:
    print(f"Sorry, {name}. You are not eligible for the scholarship.")

