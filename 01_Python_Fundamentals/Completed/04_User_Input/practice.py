# ===================================
# PRACTICE: User Input
# ===================================

# Practice 1: Ask for the user's name and greet them
name = input("What is your name? ")
print(f"Hello, {name}!")

# Practice 2: Ask for the user's favorite color and print it back
color = input("What is your favorite color? ")
print(f"Your favorite color is {color}")

# Practice 3: Ask for a number and print that number
num = input("Give me a number: ")
print(num)

# Practice 4: Ask for a number, convert to int, add 10 to it, print result
number = int(input("Give me a number: "))
print(number + 10)

# Practice 5: Ask for two numbers, convert both to int, multiply them
a = int(input("Give me a number: "))
b = int(input("Give me another number: "))
print(a * b)

# Practice 6: Ask for price and quantity, calculate total cost
price = float(input("What is the price? "))
quantity = int(input("How many? "))
print(price * quantity)

# Practice 7: Ask for temperature in Celsius, convert to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius = float(input("What is the temperature in Celsius? "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

# Challenge: Create a simple calculator
# Ask for two numbers and add them together
a = float(input("Give me a number: "))
b = float(input("Give me another number: "))
print(f"{a} + {b} = {a + b}")
