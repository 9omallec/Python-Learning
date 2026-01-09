# ===================================
# LESSON 7B: While Loops
# ===================================

# While loops repeat AS LONG AS a condition is True
# They're different from for loops - you don't know how many times they'll run!

# ===================================
# Basic While Loop
# ===================================

# Count to 5 using a while loop
count = 1

while count <= 5:
    print(count)
    count += 1  # VERY IMPORTANT: Update the variable!

print("Done!")

# ===================================
# For Loop vs While Loop
# ===================================

# Same thing with a for loop:
for count in range(1, 6):
    print(count)

# When to use which?
# - FOR loop: When you know how many times to repeat
# - WHILE loop: When you repeat until a condition changes

# ===================================
# DANGER: Infinite Loops
# ===================================

# If you forget to update the variable, the loop never ends!

# DON'T RUN THIS:
# count = 1
# while count <= 5:
#     print(count)
#     # Forgot to add count += 1
#     # This will print 1 forever!

# If you get stuck in an infinite loop, press Ctrl+C to stop it!

# ===================================
# While Loop with User Input
# ===================================

# Keep asking until they enter the correct password
password = ""

while password != "secret":
    password = input("Enter password: ")

print("Access granted!")

# Keep asking until they enter a number
valid_input = False

while not valid_input:
    age = input("Enter your age: ")
    if age.isdigit():  # Check if it's a number
        valid_input = True
        print(f"You are {age} years old")
    else:
        print("Please enter a valid number")

# ===================================
# Using a Counter
# ===================================

# Print "Hello" 3 times using while
counter = 0

while counter < 3:
    print("Hello")
    counter += 1

# ===================================
# Using a Flag Variable
# ===================================

# A flag is a True/False variable that controls the loop
keep_going = True
attempts = 0

while keep_going:
    attempts += 1
    print(f"Attempt {attempts}")

    if attempts >= 3:
        keep_going = False

print("Stopped after 3 attempts")

# ===================================
# While Loop with Conditions
# ===================================

# Count up until reaching a target
number = 0

while number < 100:
    number += 10
    print(number)

# Countdown
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Liftoff!")

# ===================================
# While True with Break
# ===================================

# while True creates an infinite loop
# break exits the loop

# This is a VERY common pattern!
while True:
    response = input("Type 'quit' to exit: ")
    if response == "quit":
        break  # Exit the loop immediately!
    print(f"You typed: {response}")

print("Loop ended!")

# Why use this pattern?
# - Simple structure
# - Check for exit at any point
# - Clear where the loop exits

# Calculator example with while True:
while True:
    first = input("Enter a number (or 'quit'): ")

    if first == "quit":
        break  # Exit here!

    x = int(first)  # Safe to convert now
    y = int(input("Enter another number: "))
    op = input("Operation (+, -, *, /): ")

    if op == "+":
        print(f"{x} + {y} = {x + y}")
    elif op == "-":
        print(f"{x} - {y} = {x - y}")
    elif op == "*":
        print(f"{x} * {y} = {x * y}")
    elif op == "/":
        print(f"{x} / {y} = {x / y}")

    # Loop automatically goes back to the top!

print("Calculator closed!")

# ===================================
# Practical Examples
# ===================================

# Simple menu system
choice = ""

while choice != "quit":
    choice = input("Enter a command (or 'quit' to exit): ")
    if choice == "hello":
        print("Hello there!")
    elif choice == "bye":
        print("Goodbye!")
    elif choice != "quit":
        print("Unknown command")

# Guessing game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("You got it!")
