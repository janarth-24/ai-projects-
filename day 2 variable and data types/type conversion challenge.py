"""
Question 3 — Type Conversion Challenge
Get a user's birth year as text, convert it to an integer, calculate their approximate age in 2026, and display the original and converted data types.
Requirements: Use input(), int(), type(), and an f-string. Consider what happens with an invalid birth year.
"""
name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")
if not birth_year.isdigit():
    print("Invalid input. Please enter a valid birth year as a number.")
    exit()
birth_year = int(birth_year)

#age calculation
if birth_year < 0:
    print("Invalid birth year entered. Please enter a valid year.")
else:  
    age = 2026 - birth_year
    print("============USER DETAILS ============")
    print(f"Name: {name}")
    print(f"Birth Year: {birth_year}")
    print(f"Data Type of Birth Year: {type(birth_year)}")
    print(f"Approximate Age in 2026: {age}")
    print(f"Data Type of Age: {type(age)}")
    print("========================================")