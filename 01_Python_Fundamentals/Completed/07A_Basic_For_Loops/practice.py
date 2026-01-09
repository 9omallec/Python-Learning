# ===================================
# PRACTICE: Basic For Loops
# ===================================

# Practice 1: Print "Hello" 5 times
for i in range(0, 6):
    print("Hello")

# Practice 2: Print numbers 0-4 using range(5)
for i in range(5):
    print(i)

# Practice 3: Print numbers 1-10 using range(1, 11)
for i in range (1, 11):
    print(i)

# Practice 4: Print even numbers from 0-10 using range(0, 11, 2)
for i in range(0, 11, 2):
    print(i)

# Practice 5: Loop through a string and print each letter
string = "Hello World"
for letter in string:
    print(letter)

# Practice 6: Print numbers 10 down to 1 using range()
for i in range (10, 0, -1):
    print(i)

# Practice 7: Calculate sum of numbers 1-5 using a loop
sum = 0
for i in range(0, 6):
    sum = sum + i
    print(f"Sum: {sum}")

# Challenge: Print a simple multiplication table for 3
for i in range(0, 21):
    sum = 3 * i
    print(f"3 * {i} = {sum}")
