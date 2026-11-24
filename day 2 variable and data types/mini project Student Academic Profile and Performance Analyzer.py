"""
## Day 2 mini project

**Student Academic Profile and Performance Analyzer**

Build a Python program that accepts a student's name, age, three subject marks, and enrollment status. Calculate the total, average, and whether the student passed (average at least 50). Display a formatted report showing the values and their data types.

Test valid inputs, decimal marks, zero marks, and invalid numeric input."""

#Collecting student details 
name = input("Enter your name: ")
age = input("Enter your age: ")
dept = input("Enter your department: ")
college = input("Enter your college name: ")
subject1 = input("Enter marks for Subject 1: ")
subject2 = input("Enter marks for Subject 2: ")
subject3 = input("Enter marks for Subject 3: ")
enrollment_status = input("Enter your enrollment status (True or False): ")

#validating and converting name 
if not name .isalpha():
    print("Invalid input. Please enter a valid name.")
    exit()
name = name.upper()

#Validating and converting age
if not age.isdigit():
    print("Invalid input. Please enter a valid age as a number.")
    exit()
age = int(age)

#validating and converting subject marks 
if not subject1.isdigit() or not subject2.isdigit() or not subject3.isdigit():
    print("Invalid input. Please enter valid marks as numbers.")
    exit()
subject1 = float(subject1)
subject2 = float(subject2)
subject3 = float(subject3)

#validating and converting enrollment status
if enrollment_status.lower() == 'true':
    enrollement_status = True
elif enrollment_status.lower() == 'false':
    enrollment_status = False
else:
    print("Invalid input. Please enter True or False for enrollment status.")
    exit()

#Caculating total, average and pass/fail status
total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
if average_marks >= 50:
    pass_status = "Pass"
else:
    pass_status = "Fail"    

#Determine the boolean pass status 
if pass_status == "Pass":
    pass_status_bool = True
else:
    pass_status_bool = False

#displaying the student academic profile and performance report
print("============STUDENT ACADEMIC PROFILE AND PERFORMANCE REPORT ============")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Department : {dept}")
print(f"College : {college}")
print(f"Enrollment Status : {enrollment_status}")

print("\n============STUDENT MARKS DETAILS ============ ")
print(f"Subject 1 Marks : {subject1}")
print(f"Subject 2 Marks : {subject2}")
print(f"Subject 3 Marks : {subject3}")
print(f"Total Marks : {total_marks}")
print(f"Average Marks : {average_marks}")
print(f"Pass/Fail Status : {pass_status}")
print(f"Boolean Pass Status : {pass_status_bool}")

print("\n============DATA TYPES ============ ")
print(f"Name : {type(name)}")
print(f"ge : {type(age)}")   
print(f"Department : {type(dept)}")
print(f"College : {type(college)}")
print(f"Enrollment Status : {type(enrollment_status)}")
print(f"Subject 1 Marks : {type(subject1)}")
print(f"Subject 2 Marks : {type(subject2)}")
print(f"Subject 3 Marks : {type(subject3)}")  
print(f"Total Marks : {type(total_marks)}")
print(f"Average Marks : {type(average_marks)}")
print(f"Pass/Fail Status : {type(pass_status)}")
print(f"Boolean Pass Status : {type(pass_status_bool)}")
print("========================================")
