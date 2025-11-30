# ===================================
# PRACTICE: If/Else Statements
# ===================================

# Practice 1: Check if a number is greater than 10
num = int(input("Give me a number. "))

if num > 10:
    print(f"{num} is greater than 10")
elif num <= 10:
    print(f"{num} is not great than 10")

# Practice 2: Check if a number is even or odd (use %)
numb = int(input("Give me a number. "))

if numb % 2 == 1:
    print(f"{numb} is odd. ")
elif numb % 2 == 0:
    print(f"{numb} is even. ")
# Practice 3: Ask user their age, check if they're 18 or older
age = int(input("What's youre age? "))

if age >= 18:
    print("You are of age. ")
elif age < 18:
    print("You are young. ")

# Practice 4: Ask for a grade (0-100), print "Pass" or "Fail" (60+ is passing)
grade = int(input("What is your grade? "))

if grade >= 60:
    print("You pass! ")
elif grade < 60:
    print("You fail! ")

# Practice 5: Check if a number is positive, negative, or zero
number = 10

if number == 0:
    print("Zero. ")
elif number < 0:
    print("Negative. ")
elif number > 0:
    print("Positive. ")

# Practice 6: Ask for temperature, print "hot" (>80), "nice" (60-80), or "cold" (<60)
temp = int(input("What is the temperature? "))

if temp > 80:
    print("Hot")
elif temp < 60:
    print("Cold")
elif 60 <= temp <= 80:
    print("Nice")
    
# Practice 7: Ask for password, check if it equals "secret123"
password = input("Enter your password: ")

if password == "secret123":
    print("Correct. ")
elif password != "secret123":
    print("Incorrect. ")

# Practice 8: Ask for age and if they have a license (yes/no)
# Determine if they can drive
age = int(input("What is your age? "))
license = input("Do you have a license? ")

if age <= 15 or license != "Yes":
    print(" You cannot drive. ")
else : print("You can drive. ")

# Challenge: Create a voting eligibility checker
# Ask for name and age
# If 18+: print "{name}, you can vote!"
# If under 18: print "{name}, you can vote in {X} years"
name = input("What is your name? ")
age = int(input("What is your age?"))

if age < 18:
    print(f"{name}, you can vote in {18 - age} years. ")
elif age >= 18:
    print(f"{name}, you can vote! ")