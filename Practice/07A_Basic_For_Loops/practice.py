# ===================================
# PRACTICE: Basic For Loops
# ===================================

# Practice 1: Print your name 5 times
for i in range(5):
    print("Connor")

# Practice 2: Print numbers from 0 to 9
for i in range(10):
    print(i)

# Practice 3: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Practice 4: Print numbers from 5 to 15
for i in range(5, 16):
    print(i)

# Practice 5: Print "Loop number X" for numbers 1 to 5
# Example output: "Loop number 1", "Loop number 2", etc.
for i in range(1, 6):
    print(f"Loop number {i}")

# Practice 6: Print all even numbers from 0 to 20
# Hint: Use range(0, 21, 2)
for i in range(0, 21, 2):
    print(i)

# Practice 7: Print all odd numbers from 1 to 19
# Hint: Use range(1, 20, 2)
for i in range(1, 20, 2):
    print(i)

# Practice 8: Count backwards from 10 to 1, then print "Done!"
for i in range(10, 0, -1):
    print(i)
print("Done!")

# Practice 9: Print the 3 times table (3, 6, 9, 12... up to 30)
# Hint: Use range(3, 31, 3) OR multiply i by 3
for i in range(3, 31, 3):
    print(i)

# Practice 10: Ask the user for a number, then print that number's times table
# Example: If they enter 7, print 7x1=7, 7x2=14, etc. up to 7x10
number = int(input("Give me a number."))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Challenge: Create a countdown timer
# Ask user for number of seconds
# Count down from that number to 1, then print "Blastoff!"
sec = int(input("How many Seconds?"))

for i in range(sec, 0, -1):
    print(i)

print("Blastoff!")