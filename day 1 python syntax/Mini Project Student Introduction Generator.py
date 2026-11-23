
"""
Problem Statement
Write a Python program that collects a student's personal and academic information and generates a well-formatted student introduction.

Requirements:
1. Get the student's full name using input().
2. Get the student's age and convert it into an integer.
3. Get the student's college name.
4. Get the student's department.
5. Get the student's current year of study.
6. Get the student's career goal (e.g., AI Engineer, Data Scientist).
7. Check whether the entered age is valid (greater than 0).
8. Check whether the student's name is empty.
9. Display all details using f-strings.
10. Include at least two meaningful Python comments.
"""
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
college_name = input("Enter your college name: ")
department = input("Enter your department: ")
year_of_study = input("Enter your current year of study: ")
career_goal = input("Enter your career goal (e.g., AI Engineer, Data Scientist): ")

#Check the age is valid or not 
if age <=0:
    print("Please enter a valid age greater than 0.")
 #check name is empty or not
elif name.strip() == "":
    print("Please enter a valid name.")
else:
    print("\n========== STUDENT PROFILE ==========")
    print(f"Name        : {name}")
    print(f"Age         : {age}")
    print(f"College     : {college_name}")
    print(f"Department  : {department}")
    print(f"Year        : {year_of_study}")
    print(f"Career Goal : {career_goal}")

    print(f"\nWelcome, {name}!")
    print(f"Your goal is to become an {career_goal}.")

    print("\n=====================================")
