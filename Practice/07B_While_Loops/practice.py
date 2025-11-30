# ===================================
# PRACTICE: While Loops
# ===================================

# Practice 1: Print numbers 1 to 5 using a while loop
count = 1

while count <=5:
    print(count)
    count += 1

# Practice 2: Count down from 10 to 1 using a while loop
count = 10

while count >=1:
    print(count)
    count -= 1

# Practice 3: Ask user for their name, keep asking until they enter something
# Hint: Use while name == ""
name = ""

while name == "":
    name = input("What is your name? ")

print(f"Hello {name}")

# Practice 4: Ask for a password, keep asking until they enter "python123"
password = ""

while password != "python123":
    password = input("What is the password: ")

# Practice 5: Print "Hello" 10 times using a while loop with a counter
count = 1

while count != 11:
    count += 1
    print("Hello!")

# Practice 6: Ask user for a number, keep doubling it until it's greater than 100
# Print the number each time
num = int(input("Give me a number "))

while num <= 100:
    num *= 2
    print(f"{num}")


# Practice 7: Create a simple calculator that keeps running until user types "quit"
# Ask for two numbers and an operation (+, -, *, /)
while True:
    first = input("Give me a number or 'quit': ")

    if first == "quit":
        break
    elif first != "quit":
        x = int(first)
        y = int(input("Give me another number "))
        op = input("Would you like to (*, /, +, -) ")
    if op == "*":
        print(f"{x} * {y} = {x * y}")
    elif op == "/":
        print(f"{x} / {y} = {x / y}")
    elif op == "+":
        print(f"{x} + {y} = {x + y}")
    elif op == "-":
        print(f"{x} - {y} = {x - y}")


# Practice 8: Count how many times user enters "yes"
# Stop when they enter "stop" and print the total count
count = 0

while True:

    i = input("Type 'yes' as many times as you like or 'stop' ")


    if i == "yes":
        count += 1
    if i == "stop":
        break

print(count)

# Challenge: Create a number guessing game
# Computer picks a random number 1-10 (you can just hard-code 7)
# User keeps guessing until correct
# Give hints: "too high" or "too low"
# At the end, tell them how many guesses it took
count = 0
answer = 7

while True:
    count += 1
    guess = int(input("Pick a number from 1-10: "))
    if guess != 7:
        print("Try again! ")
    if guess < 7:
        print("Too low! ")
    if guess > 7:
        print("Too High! ")
    elif guess == 7:
        print(f"Correct! it took you {count} number of tries" )
        break
