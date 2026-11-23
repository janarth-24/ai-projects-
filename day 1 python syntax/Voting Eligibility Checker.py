"""
Problem Statement
Write a Python program that checks whether a person is eligible to vote based on their age.
Requirements
1. Get the person's name using input().
2. Get the person's age using input().
3. Convert the age into an integer using int().
4. Check whether the age is 18 or above.
5. If the age is 18 or above, display a voting eligibility message.
6. If the age is below 18, display a not-eligible message.
7. If the age is negative, display an invalid-age message.
8. Display the result using an f-string.
9. Include at least one Python comment.
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check voting eligibility based on age

if age>=18:
    print(f"{name}, you are eligible to vote.")
elif age>0 and age<18:
    print(f"{name}, you are not eligible to vote.")
elif age<0:
    print(f"{name}, you have entered an invalid age.")
else:
    print("Enter a valid input.")
