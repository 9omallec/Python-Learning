# ===================================
# LESSON 7: Loops (for and while)
# ===================================

# Loops let you repeat code multiple times
# This is one of the most powerful concepts in programming!

# ===================================
# FOR LOOPS
# ===================================

# Print something 5 times
for i in range(5):
    print("Hello!")

# range(5) creates numbers: 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# You can specify start and end
for i in range(1, 6):  # Start at 1, stop before 6
    print(i)  # Prints: 1, 2, 3, 4, 5

# You can specify a step (count by 2s, 10s, etc.)
for i in range(0, 11, 2):  # Start at 0, stop before 11, step by 2
    print(i)  # Prints: 0, 2, 4, 6, 8, 10

# Count backwards
for i in range(10, 0, -1):
    print(i)

# Loop through a string
name = "Connor"
for letter in name:
    print(letter)

# Use the loop variable in calculations
for i in range(1, 6):
    print(f"{i} times 2 is {i * 2}")

# ===================================
# WHILE LOOPS
# ===================================

# While loops repeat as long as a condition is True
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # IMPORTANT: Always update the variable!

# Asking for input until correct answer
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Using a flag variable
keep_going = True
counter = 0

while keep_going:
    counter += 1
    print(f"Counter: {counter}")

    if counter >= 3:
        keep_going = False

# ===================================
# BREAK and CONTINUE
# ===================================

# break: Exit the loop early
for i in range(10):
    if i == 5:
        break  # Stop the loop when i is 5
    print(i)  # Prints: 0, 1, 2, 3, 4

# continue: Skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)  # Prints: 0, 1, 3, 4

# Practical example: Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Only prints odd: 1, 3, 5, 7, 9

# ===================================
# NESTED LOOPS
# ===================================

# A loop inside another loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Create a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
