# Python Quick Reference Guide

## Print
```python
print("Hello")              # Print text
print(42)                   # Print number
print("I am", 25)          # Print multiple things
```

## Variables
```python
name = "Connor"             # String (text)
age = 25                    # Integer (whole number)
height = 5.9               # Float (decimal)
is_student = True          # Boolean (True/False)
```

## Math Operations
```python
10 + 3      # Addition: 13
10 - 3      # Subtraction: 7
10 * 3      # Multiplication: 30
10 / 3      # Division: 3.333...
10 // 3     # Integer Division: 3
10 % 3      # Remainder: 1
10 ** 3     # Power: 1000

x += 5      # Same as: x = x + 5
x -= 5      # Same as: x = x - 5
x *= 5      # Same as: x = x * 5
x /= 5      # Same as: x = x / 5
```

## User Input
```python
name = input("What's your name? ")          # Returns string
age = int(input("What's your age? "))       # Convert to integer
height = float(input("Your height? "))      # Convert to float
```

## Strings
```python
text = "Hello World"

text.upper()            # "HELLO WORLD"
text.lower()            # "hello world"
text.replace("H", "J")  # "Jello World"
len(text)               # 11 (length)

# Combining strings:
first = "John"
last = "Doe"
full = first + " " + last           # Using +
full = f"{first} {last}"            # Using f-string (BEST!)

# String indexing:
word = "Python"
word[0]     # "P" (first character)
word[-1]    # "n" (last character)
word[0:3]   # "Pyt" (slice)
```

## If/Else Statements
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Comparison operators:
# >   greater than
# <   less than
# >=  greater or equal
# <=  less or equal
# ==  equal to
# !=  not equal to

# Combining conditions:
if age >= 16 and has_license:
    print("Can drive")

if day == "Sat" or day == "Sun":
    print("Weekend!")
```

## Common Patterns

### Get a number from user and do math
```python
num = int(input("Enter a number: "))
result = num * 2
print(f"Double is {result}")
```

### Check if even or odd
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Simple calculator
```python
x = int(input("First number: "))
y = int(input("Second number: "))
print(f"{x} + {y} = {x + y}")
```

## Tips for Beginners

1. **Strings vs Numbers**: Use quotes for text, no quotes for numbers
   - `name = "Connor"` (string)
   - `age = 25` (number)

2. **input() returns a string**: Always convert if you need a number!
   - `age = int(input("Age? "))`

3. **Indentation matters**: Code inside if/else must be indented (4 spaces)

4. **Use f-strings**: They're the easiest way to combine text and variables
   - `print(f"I am {age} years old")`

5. **= vs ==**: One equal sign assigns, two equal signs compares
   - `x = 5` (assignment)
   - `if x == 5:` (comparison)
