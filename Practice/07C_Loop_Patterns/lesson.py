# ===================================
# LESSON 7C: Loop Patterns
# ===================================

# Common patterns you'll use all the time!

# ===================================
# Looping Through a String
# ===================================

# You can loop through each letter in a string
name = "Connor"

for letter in name:
    print(letter)

# Output:
# C
# o
# n
# n
# o
# r

# Practical use: Count vowels
word = "Python"
vowel_count = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"Vowels: {vowel_count}")

# ===================================
# Accumulator Pattern (Building Up a Total)
# ===================================

# Calculate sum of 1 + 2 + 3 + 4 + 5
total = 0

for i in range(1, 6):
    total += i
    print(f"Adding {i}, total is now {total}")

print(f"Final total: {total}")

# Sum of all numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i

print(f"Sum of 1-100: {total}")

# ===================================
# Building a String
# ===================================

# Build a string by adding to it
result = ""

for i in range(5):
    result += "X"
    print(result)

# Output:
# X
# XX
# XXX
# XXXX
# XXXXX

# ===================================
# Counting Pattern
# ===================================

# Count how many even numbers in range
even_count = 0

for i in range(1, 21):
    if i % 2 == 0:
        even_count += 1

print(f"There are {even_count} even numbers from 1-20")

# Count how many times a letter appears
text = "hello world"
count = 0

for letter in text:
    if letter == "l":
        count += 1

print(f"The letter 'l' appears {count} times")

# ===================================
# Finding Maximum/Minimum
# ===================================

# Find the largest number someone enters
largest = 0

for i in range(5):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print(f"The largest number was {largest}")

# ===================================
# User Input in a Loop
# ===================================

# Ask for 5 names and greet each one
for i in range(5):
    name = input("Enter a name: ")
    print(f"Hello, {name}!")

# Better version: show which number
for i in range(1, 6):
    name = input(f"Enter name {i}: ")
    print(f"Hello, {name}!")

# ===================================
# Skip Certain Values
# ===================================

# Print all numbers 1-10 except 5
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest and go to next iteration
    print(i)

# Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# ===================================
# Practical Examples
# ===================================

# Calculate average of user inputs
total = 0
count = 5

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num

average = total / count
print(f"Average: {average}")

# Print a pattern
for i in range(1, 6):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****

# Reverse a word
word = "Python"
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

print(reversed_word)  # nohtyP
