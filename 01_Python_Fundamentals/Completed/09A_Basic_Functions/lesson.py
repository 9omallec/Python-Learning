# ===================================
# LESSON 9A: Basic Functions
# ===================================

# Functions are reusable blocks of code
# They help you avoid repeating yourself!

# ===================================
# DEFINING A FUNCTION
# ===================================

# Basic function - no parameters
def greet():
    print("Hello!")
    print("Welcome to Python!")

# Call the function
greet()
greet()  # Can call it multiple times!

# ===================================
# FUNCTION WITH ONE PARAMETER
# ===================================

def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")

# Call with different arguments
greet_person("Connor")
greet_person("Alice")
greet_person("Bob")

# ===================================
# FUNCTION WITH TWO PARAMETERS
# ===================================

def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)   # 5 + 3 = 8
add_numbers(10, 20) # 10 + 20 = 30

def greet_full(first, last):
    print(f"Hello, {first} {last}!")

greet_full("Connor", "O'Malley")

# ===================================
# WHY USE FUNCTIONS?
# ===================================

# WITHOUT FUNCTIONS - Lots of repetition!
print("=" * 30)
print("    WELCOME TO MY PROGRAM")
print("=" * 30)

print("=" * 30)
print("    WELCOME TO MY PROGRAM")
print("=" * 30)

# WITH FUNCTIONS - Write once, use many times!
def print_header():
    print("=" * 30)
    print("    WELCOME TO MY PROGRAM")
    print("=" * 30)

print_header()
print_header()

# ===================================
# FUNCTIONS THAT RETURN VALUES
# ===================================

# This function RETURNS a value instead of printing
def add(a, b):
    return a + b

# Save the returned value
result = add(5, 3)
print(result)  # 8

# Use it directly
print(add(10, 20))  # 30

# Use in calculations
total = add(5, 3) + add(10, 2)
print(total)  # 8 + 12 = 20

# ===================================
# PRINT vs RETURN
# ===================================

# This function PRINTS
def greet_print(name):
    print(f"Hello, {name}")

# This function RETURNS
def greet_return(name):
    return f"Hello, {name}"

# Example of difference:
greet_print("Bob")  # Prints "Hello, Bob"
message = greet_return("Bob")  # Returns "Hello, Bob"
print(message)  # Now we can print it
print(message.upper())  # And use the returned value!

# ===================================
# PRACTICAL EXAMPLES
# ===================================

# Calculate rectangle area
def calculate_area(length, width):
    area = length * width
    return area

room_area = calculate_area(10, 12)
print(f"Room area: {room_area} square feet")

# Check if number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # True
print(is_even(7))  # False

# Temperature converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temp = celsius_to_fahrenheit(25)
print(f"25°C = {temp}°F")

# ===================================
# CALLING FUNCTIONS FROM FUNCTIONS
# ===================================

def double(n):
    return n * 2

def quadruple(n):
    return double(double(n))  # Call double twice!

print(quadruple(5))  # 5 -> 10 -> 20

# ===================================
# COMMON PATTERNS
# ===================================

# Validation function
def is_valid_age(age):
    if age >= 0 and age <= 120:
        return True
    return False

user_age = 25
if is_valid_age(user_age):
    print("Valid age!")

# Calculation function
def calculate_total(subtotal, tax_rate):
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

bill = calculate_total(50, 0.08)
print(f"Total bill: ${bill}")

# Formatting function
def format_name(first, last):
    return f"{last}, {first}"

formatted = format_name("Connor", "O'Malley")
print(formatted)  # O'Malley, Connor
