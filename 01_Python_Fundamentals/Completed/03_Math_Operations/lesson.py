# ===================================
# LESSON 3: Math Operations
# ===================================

# Python can do math!
x = 10
y = 3

# Basic operations:
print("Addition:", x + y)           # 13
print("Subtraction:", x - y)        # 7
print("Multiplication:", x * y)     # 30
print("Division:", x / y)           # 3.333...

# Special operations:
print("Integer Division:", x // y)  # 3 (rounds down, no decimal)
print("Remainder (Modulo):", x % y) # 1 (what's left over)
print("Power:", x ** y)             # 1000 (10 to the power of 3)

# Order of operations (PEMDAS):
result = 2 + 3 * 4
print("2 + 3 * 4 =", result)  # 14 (multiplication first)

result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)  # 20 (parentheses first)

# You can do math with variables:
price = 19.99
quantity = 3
total = price * quantity
print("Total:", total)

# You can update variables using math:
counter = 0
counter = counter + 1  # Add 1 to counter
print("Counter:", counter)

# Shorthand for updating:
counter += 1  # Same as: counter = counter + 1
print("Counter:", counter)

counter -= 1  # Subtract 1
counter *= 2  # Multiply by 2
counter /= 2  # Divide by 2

# ===================================
# Useful Math Functions
# ===================================

# round() - Round decimals
price = 19.567
print(round(price))       # 20 (rounds to whole number)
print(round(price, 2))    # 19.57 (rounds to 2 decimal places)
print(round(price, 1))    # 19.6 (rounds to 1 decimal place)

# abs() - Absolute value (always positive)
temperature = -15
print(abs(temperature))   # 15

difference = -50
print(abs(difference))    # 50

# IMPORTANT: int() truncates, doesn't round!
print(int(3.9))   # 3 (just removes decimal, doesn't round!)
print(round(3.9)) # 4 (this actually rounds)

# max() and min() - find largest/smallest
print(max(5, 10, 3))  # 10
print(min(5, 10, 3))  # 3
