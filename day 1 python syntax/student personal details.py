"""
Question 1: Student Personal Details
Write a Python program to store and display a student's personal information.

Requirements:
1. Store the student's name, age, college name, and department using variables.
2. Use appropriate data types.
3. Display the information in a readable format.
4. Include at least one Python comment."""
name=input("Enter your name: ")
age=int(input("Enter your age: "))
clg=input("Enter your college name: ")
dept=input("Enter your department: ")
print(f"Your name is {name}. Your age is {age}. You are studying in {clg} in the department of {dept}.")