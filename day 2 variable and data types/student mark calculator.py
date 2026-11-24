"""
Question 2 — Student Marks Calculator
Accept marks for three subjects using input(). Convert them into numeric values, calculate the total and average, and display the results.
Requirements: Use int() or float(), arithmetic operators, and f-strings. Test decimal marks.
"""
name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")
subject1 =float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

print("============STUDENT MARKS DETAILS ============")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Total Marks: {total_marks}")
print("========================================")