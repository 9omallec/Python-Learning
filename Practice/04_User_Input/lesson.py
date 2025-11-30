# ===================================
# LESSON 4: User Input
# ===================================

# The input() function asks the user for information
# Whatever they type is stored as a string (text)

user_name = input("What is your name? ")
print("Nice to meet you,", user_name)

user_age = input("How old are you? ")
print("You are", user_age, "years old!")

# IMPORTANT: input() always returns a STRING!
# Even if the user types a number, it's still text

# This is a problem if you want to do math:
# favorite_number = input("What's your favorite number? ")
# doubled = favorite_number * 2  # This would cause an error!

# SOLUTION: Convert the string to an integer using int()
favorite_number = input("What's your favorite number? ")
favorite_number = int(favorite_number)  # Convert to integer
doubled = favorite_number * 2
print("Your favorite number doubled is:", doubled)

# You can convert on the same line:
age = int(input("Enter your age: "))
next_year = age + 1
print("Next year you'll be", next_year)

# Converting to float (decimal numbers):
height = float(input("Enter your height in feet: "))
height_cm = height * 30.48
print("That's", height_cm, "centimeters")
