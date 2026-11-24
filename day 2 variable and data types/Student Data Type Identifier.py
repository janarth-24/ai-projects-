"""
Question 1 — Student Data Type Identifier

Write a program that stores a student's name, age, percentage, and enrollment status. Display each value and its data type using type().
Requirements: Use str, int, float, and bool, meaningful variable names, and f-strings
"""
name = input("Enter your name: ")
age= int(input("Enter you age: "))
percentage = float(input("Enter your percentage: "))
enrollment_status= input("Enter you are Enrolled (True or False): ")

if enrollment_status.lower() == 'true':
    enrollment_status = True
else:
    enrollment_status = False

print("============STUDENT DETAILS ============")
print(f"Name        : {name}")
print(f"Data Type   : {type(name)}")
print(f"Age         : {age}")
print(f"Data Type   : {type(age)}")
print(f"Percentage  : {percentage}")
print(f"Data Type   : {type(percentage)}")
print(f"Enrollment Status: {enrollment_status}")
print(f"Data Type   : {type(enrollment_status)}")
print("========================================")
