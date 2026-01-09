# ===================================
# PRACTICE: If/Else Statements
# ===================================

# Practice 1: Check if a number is greater than 10
number = 15
if number > 10:
    print("That is greater than 10!")

# Practice 2: Check if a number is even or odd (use %)
number = 13
if number % 2 == 0:
    print("That is an even number?")
else:
    print("That is an odd number")


# Practice 3: Ask user their age, check if they're 18 or older
age = int(input("What is your age? "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a child")

# Practice 4: Ask for a grade (0-100), print "Pass" or "Fail" (60+ is passing)
grade = int(input("What is your grade? "))
if grade >= 60:
    print("You passed!")
else:
    print("You failed")

# Practice 5: Check if a number is positive, negative, or zero
number = 13
if number > 0:
    print("That is a positive number")
elif number < 0:
    print("That is a negative number")
else:
    print("That is 0")

# Practice 6: Ask for temperature, print "hot" (>80), "nice" (60-80), or "cold" (<60)
temp = int(input("What is the temperature? "))
if temp > 80:
    print("Hot")
elif 60 <= temp <= 80:  # Pythonic chained comparison
    print("Nice")
else:
    print("Cold")

# Practice 7: Ask for password, check if it equals "secret123"
pword = input("What is the password? ")
if pword == "secret123":
    print("Correct!")
else:
    print("Incorrect")

# Practice 8: Ask for age and if they have a license (yes/no)
# Determine if they can drive
age = int(input("What is your age? "))
license = input("Do you have a license? ")
if age >= 16 and license.lower() == "yes":
    print("You can drive!")
else:
    print("You cannot drive")

# Challenge: Create a voting eligibility checker
# Ask for name and age
# If 18+: print "{name}, you can vote!"
# If under 18: print "{name}, you can vote in {X} years"
name = input("What is your name? ")
age = int(input("What is your age? "))
almost = 18 - age
if age >= 18:
    print(f"{name}, You can vote! ")
else:
    print(f"{name}, you can vote in {almost} years! ")

