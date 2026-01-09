# ===================================
# LESSON 7A: Basic For Loops
# ===================================

# Loops let you repeat code multiple times
# This saves you from writing the same thing over and over!

# ===================================
# WITHOUT A LOOP (The Hard Way)
# ===================================

# If you want to print "Hello" 5 times:
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# That's annoying! There's a better way...

# ===================================
# WITH A LOOP (The Easy Way)
# ===================================

# Print "Hello" 5 times using a loop
for i in range(5):
    print("Hello")

# Much easier!

# ===================================
# Understanding range()
# ===================================

# range(5) creates numbers: 0, 1, 2, 3, 4
# Let's see what numbers it creates:

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Notice: It starts at 0 and stops BEFORE 5

# ===================================
# Counting from 1 to 10
# ===================================

# If you want to count 1, 2, 3... you specify start and stop
for i in range(1, 11):  # Start at 1, stop BEFORE 11
    print(i)

# This prints: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# ===================================
# Using the Loop Variable
# ===================================

# The variable (i) changes each time through the loop
# You can use it in your code!

for i in range(1, 6):
    print(f"Loop number {i}")

# You can do math with it:
for i in range(1, 6):
    print(f"{i} times 2 is {i * 2}")

# ===================================
# Counting by Different Amounts
# ===================================

# Count by 2s (even numbers)
for i in range(0, 11, 2):  # Start, stop, step
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# Count by 5s
for i in range(0, 26, 5):
    print(i)
# Output: 0, 5, 10, 15, 20, 25

# Count by 10s
for i in range(10, 101, 10):
    print(i)
# Output: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

# ===================================
# Counting Backwards
# ===================================

# Countdown from 10 to 1
for i in range(10, 0, -1):  # Start at 10, stop before 0, step by -1
    print(i)

print("Blastoff!")

# ===================================
# IMPORTANT: Indentation
# ===================================

# Code INSIDE the loop must be indented (4 spaces or 1 tab)
for i in range(3):
    print("This is inside the loop")
    print("This is also inside the loop")

print("This is OUTSIDE the loop - only runs once")

# ===================================
# Practical Examples
# ===================================

# Print a multiplication table for 5
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

# Count down for a timer
for seconds in range(5, 0, -1):
    print(f"{seconds} seconds remaining...")
print("Time's up!")

# ===================================
# Looping Through Strings
# ===================================

# You can loop through each character in a string
name = "Python"
for letter in name:
    print(letter)
# Output: P, y, t, h, o, n (each on new line)

# ===================================
# enumerate() - Get Index AND Value
# ===================================

# Sometimes you need to know WHICH iteration you're on
# enumerate() gives you both the index (position) and the value

fruits = ["apple", "banana", "orange"]

# Without enumerate (awkward):
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (better!):
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: orange

# Start counting from 1 instead of 0:
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. orange
