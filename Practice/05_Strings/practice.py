# ===================================
# PRACTICE: Strings
# ===================================

# Practice 1: Create a string and print it in UPPERCASE
greeting = "Hello World. "
print(greeting.upper())

# Practice 2: Create a string and print it in lowercase
greetings = "Hellos Worlds. "
print(greetings.lower())

# Practice 3: Create first_name and last_name, combine with +
first_name = "Connor"
last_name = "O'Malley"
print(first_name + " " + last_name)

# Practice 4: Use an f-string to print your name and age
name = "Connor"
age = 35
print(f"Hello {name} you are {age} years old.")

# Practice 5: Create a string and find its length
mid_name = "Rodney"
print(len(mid_name))

# Practice 6: Replace a word in a string with another word
print(greeting.replace("World", "Claude"))

# Practice 7: Get the first character of your name
print(name[0])

# Practice 8: Get the last character of your name
print(name[-1])

# Practice 9: Ask user for their full name, print just the first 3 letters
full_name = input("What is your full name? ")
print(full_name[:3])

# Challenge: Ask for first and last name separately
# Print them as: "Last, First" (like Rodriguez, Connor)
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
print(lastname + ", " + firstname)