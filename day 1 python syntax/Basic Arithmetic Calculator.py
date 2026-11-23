"""
Problem Statement
Write a Python program that accepts two numbers from the user and performs basic arithmetic operations.
Requirements
1. Get two numbers from the user using input().
2. Convert the inputs into appropriate numeric data types.
3. Calculate the addition of the two numbers.
4. Calculate the subtraction of the two numbers.
5. Calculate the multiplication of the two numbers.
6. Calculate the division of the two numbers.
7. Handle division by zero appropriately.
8. Display all results clearly using f-strings.
9. Include at least one Python comment.
"""
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

#convert the number into float 
first_number = float (first_number)
second_number = float (second_number)

#Addition operation 
addition = first_number + second_number 

#subtraction operation 
subtraction = first_number - second_number

#multiplication operation
multiplication = first_number * second_number   

#division operation
if second_number != 0:
    division = first_number / second_number
else:
    division = "undefined (cannot divide by zero)"      

print(f"The addition of {first_number} and {second_number} is : {addition}")
print(f"The subtraction of {first_number} and {second_number} is : {subtraction}")
print(f"The multiplication of {first_number} and {second_number} is : {multiplication}")
print(f"The division of {first_number} and {second_number} is : {division}")    

