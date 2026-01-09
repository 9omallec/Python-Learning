# ===================================
# PRACTICE: Strings
# ===================================

# Practice 1: Create a string and print it in UPPERCASE
hello = "Hello World"
print(hello.upper())

# Practice 2: Create a string and print it in lowercase
print(hello.lower())

# Practice 3: Create first_name and last_name, combine with +
first_name = "Connor"
last_name = "O'Malley"
full_name = first_name + " " + last_name

# Practice 4: Use an f-string to print your name and age
age = 35
name = "Connor"
print(f"My name is {name}, I am {age} years old")

# Practice 5: Create a string and find its length
stri = "Hello Worldz"
print(len(stri))

# Practice 6: Replace a word in a string with another word
string_6 = "In an Air BNB"
print(string_6.replace("BNB", "Hotel"))

# Practice 7: Get the first character of your name
name = "Connor"
print(name[0])

# Practice 8: Get the last character of your name
print(name[-1])

# Practice 9: Ask user for their full name, print just the first 3 letters
full_name = input("What is your full name? ")
print(full_name[0:3])

# Challenge: Ask for first and last name separately
# Print them as: "Last, First" (like O'Malley, Connor)
first = input("What is your first name? ")
last = input("What is your last name? ")
print(f"{last}, {first}")