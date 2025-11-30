# ===================================
# LESSON 6: If/Else Statements
# ===================================

# Programs need to make decisions!
# if statements let your code choose what to do

temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("It's nice weather!")
else:
    print("It's cold outside!")

# IMPORTANT: Notice the indentation (spaces before print)
# Python uses indentation to know what's inside the if statement

# Comparison operators:
# >  greater than
# <  less than
# >= greater than or equal to
# <= less than or equal to
# == equal to (TWO equal signs!)
# != not equal to

age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Combining conditions with "and" and "or":
has_license = True
age = 20

if age >= 16 and has_license:
    print("You can drive!")
elif age >= 16 and not has_license:
    print("You're old enough, but need a license")
else:
    print("You're too young to drive")

# Using "or":
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")

# Nested if statements:
grade = 85

if grade >= 60:
    print("You passed!")
    if grade >= 90:
        print("You got an A!")
    elif grade >= 80:
        print("You got a B!")
else:
    print("You failed")

# Checking if values are equal:
password = "python123"

if password == "python123":
    print("Access granted")
else:
    print("Access denied")

# ===================================
# The "in" Operator
# ===================================

# Check if something exists IN something else
if "a" in "banana":
    print("Found 'a' in banana!")

# Check if a letter is a vowel
letter = "e"
if letter in "aeiou":
    print(f"{letter} is a vowel")

# Check if word is in a sentence
sentence = "Python is awesome"
if "Python" in sentence:
    print("Found Python!")

# ===================================
# Truthiness - What Counts as True/False
# ===================================

# These values are considered FALSE:
# - 0 (zero)
# - "" (empty string)
# - None
# - False

# Everything else is TRUE!

# Example with numbers:
if 0:
    print("Won't print - 0 is False")

if 1:
    print("Will print - non-zero is True")

if -5:
    print("Will print - negative numbers are True too!")

# Example with strings:
name = ""
if name:
    print("Won't print - empty string is False")

name = "Connor"
if name:
    print("Will print - non-empty string is True")

# This is super useful for checking if user entered something:
user_input = input("Enter your name: ")
if user_input:
    print(f"Hello, {user_input}!")
else:
    print("You didn't enter anything!")

# ===================================
# Common Mistake: = vs ==
# ===================================

# = is ASSIGNMENT (sets a value)
# == is COMPARISON (checks if equal)

x = 5      # This SETS x to 5
if x == 5: # This CHECKS if x equals 5
    print("x is 5")
