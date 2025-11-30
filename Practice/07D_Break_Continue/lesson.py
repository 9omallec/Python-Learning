# ===================================
# LESSON 7D: Break and Continue
# ===================================

# break: Exit the loop completely
# continue: Skip to the next iteration

# ===================================
# The BREAK Statement
# ===================================

# Stop the loop when you find what you're looking for
for i in range(10):
    if i == 5:
        break  # Exit the loop completely
    print(i)

# Output: 0, 1, 2, 3, 4 (stops at 5)

# Practical example: Search for a number
numbers = [3, 7, 2, 9, 4, 6]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")

# ===================================
# Break with While Loops
# ===================================

# Exit a while loop early
while True:  # Infinite loop!
    response = input("Type 'quit' to exit: ")
    if response == "quit":
        break  # Exit the loop
    print(f"You said: {response}")

print("Goodbye!")

# Guessing game with limited attempts
secret = 7
attempts = 0
max_attempts = 3

while True:
    attempts += 1
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        break

    if attempts >= max_attempts:
        print(f"Out of attempts! The number was {secret}")
        break

    print("Try again!")

# ===================================
# The CONTINUE Statement
# ===================================

# Skip certain iterations
for i in range(10):
    if i == 5:
        continue  # Skip the rest of THIS iteration
    print(i)

# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9 (skips 5)

# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Output: 1, 3, 5, 7, 9

# ===================================
# Continue vs Break
# ===================================

print("Using CONTINUE:")
for i in range(5):
    if i == 2:
        continue  # Skip this one, keep going
    print(i)
# Output: 0, 1, 3, 4

print("\nUsing BREAK:")
for i in range(5):
    if i == 2:
        break  # Stop completely
    print(i)
# Output: 0, 1

# ===================================
# Practical Examples with Break
# ===================================

# Find first even number in a list
numbers = [1, 3, 5, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# Password with 3 attempts
password = "secret"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")
    attempts += 1

    if user_input == password:
        print("Access granted!")
        break
else:  # This runs if loop completes without break
    print("Access denied - too many attempts")

# ===================================
# Practical Examples with Continue
# ===================================

# Process only positive numbers
numbers = [5, -2, 3, -7, 10, -1, 8]

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(f"Processing {num}")

# Skip empty inputs
for i in range(5):
    name = input("Enter a name (or press Enter to skip): ")
    if name == "":
        continue  # Skip if empty
    print(f"Hello, {name}!")

# ===================================
# Combining Break and Continue
# ===================================

# Process numbers until you hit a negative, skip zeros
numbers = [5, 0, 3, 0, 7, -1, 10]

for num in numbers:
    if num < 0:
        print("Negative number found, stopping")
        break

    if num == 0:
        continue  # Skip zeros

    print(f"Processing {num}")

# Output:
# Processing 5
# Processing 3
# Processing 7
# Negative number found, stopping
