# ===================================
# EXTRA PRACTICE: User Input
# ===================================

# Exercise 1: Ask for first name and last name separately
# Print them together as "First Last"
first = input("What is your first name? ")
last = input("What is your last name? ")
print(f"{first} {last}")

# Exercise 2: Ask for three favorite foods
# Print them in a sentence: "Your favorites are X, Y, and Z"
first = input("What is your favorite food? ")
second = input("What is your second favorite food? ")
third = input("What is your third favorite food? ")
print(f"Your favorites are {first}, {second}, and {third}")

# Exercise 3: Create a Mad Libs game
# Ask for: adjective, noun, verb, place
# Print a funny sentence using them
adj = input("Give me an adjective: ")
noun = input("Give me a noun: ")
verb = input("Give me a verb: ")
place = input("Give me a place: ")
print(f"The {adj} {noun} decided to {verb} at the {place}!")

# Exercise 4: Ask for birth year, calculate age
# (Use 2025 as current year)
birth_year = int(input("What year were you born? "))
print(f"You are {2025 - birth_year} years old")

# Exercise 5: Ask for hours worked and hourly rate
# Calculate and print total pay
hours = float(input("How many hours have you worked? "))
rate = float(input("How much are you paid per hour? "))
print(f"Your total pay is ${hours * rate}")

# Exercise 6: Ask for item price and quantity
# Calculate total cost and print with $
price = float(input("What is the price? $"))
quantity = int(input("How many? "))
print(f"Total: ${price * quantity}")

# Exercise 7: Ask for distance in miles
# Convert to kilometers (1 mile = 1.609 km)
distance = float(input("How many miles? "))
print(f"{distance} miles is {distance * 1.609} kilometers")

# Exercise 8: Create a simple order form
# Ask for: name, item, quantity, price per item
# Print a receipt with total
name = input("What is your name? ")
item = input("What item? ")
quantity = int(input("How many? "))
price = float(input("How much $ per item? "))
total = quantity * price
print(f"\n--- RECEIPT ---")
print(f"Customer: {name}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Total: ${total}")

# Exercise 9: Ask for temperature in Fahrenheit
# Convert to Celsius and print both
# Formula: C = (F - 32) * 5/9
temp_f = float(input("What is the temperature in Fahrenheit? "))
temp_c = (temp_f - 32) * 5 / 9
print(f"{temp_f}°F is {temp_c}°C")

# Exercise 10: Ask for radius of a circle
# Calculate and print both area and circumference
# Area = 3.14 * r * r
# Circumference = 2 * 3.14 * r
radius = float(input("What is the radius of your circle? "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print(f"Area: {area}")
print(f"Circumference: {circumference}")

# Exercise 11: Ask for length and width of a rectangle
# Calculate and print: area, perimeter
length = float(input("What is the length of your rectangle? "))
width = float(input("What is the width of your rectangle? "))
area = length * width
perimeter = 2 * length + 2 * width
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Exercise 12: Create a tip calculator
# Ask for bill amount and tip percentage
# Calculate and print total with tip
bill = float(input("How much is your bill? $"))
tip_percent = float(input("What percentage would you like to tip? "))
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
print(f"Tip: ${tip_amount}")
print(f"Total: ${total}")

# Challenge: Create a simple quiz
# Ask 3 math questions (like "What is 7 + 5?")
# Don't check if correct yet (just get their answers)
# Print all their answers at the end
q1 = input("What is 2 * 2? ")
q2 = input("What is 2 * 3? ")
q3 = input("What is 2 + 4? ")
print(f"Your answers were: {q1}, {q2}, {q3}")
