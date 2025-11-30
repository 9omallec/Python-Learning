# ===================================
# LESSON 9: Functions
# ===================================

# Functions are reusable blocks of code
# They help organize your program and avoid repetition

# ===================================
# BASIC FUNCTIONS
# ===================================

# Define a function
def greet():
    print("Hello!")

# Call the function
greet()
greet()  # You can call it multiple times

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Connor")
greet_person("Alice")

# Multiple parameters
def greet_full(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full("Connor", "O'Malley")

# ===================================
# RETURN VALUES
# ===================================

# Functions can return values
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# You can use the return value directly
print(add(10, 20))  # 30

# Multiple calculations
def calculate(x, y):
    sum_result = x + y
    product = x * y
    return sum_result, product  # Returns a tuple

s, p = calculate(5, 3)
print(f"Sum: {s}, Product: {p}")

# ===================================
# DEFAULT PARAMETERS
# ===================================

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Connor")  # Hello, Connor!
greet()          # Hello, Guest!

def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# ===================================
# KEYWORD ARGUMENTS
# ===================================

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

# Positional arguments
describe_pet("dog", "Rex")

# Keyword arguments (can be in any order)
describe_pet(name="Fluffy", animal="cat")

# ===================================
# RETURN VS PRINT
# ===================================

# PRINT: Just displays, doesn't give back a value
def greet_print(name):
    print(f"Hello, {name}")

# RETURN: Gives back a value you can use
def greet_return(name):
    return f"Hello, {name}"

# Example of the difference:
greet_print("Bob")  # Prints "Hello, Bob", returns None
message = greet_return("Bob")  # Returns "Hello, Bob"
print(message.upper())  # Can use the returned value!

# ===================================
# PRACTICAL EXAMPLES
# ===================================

# Check if number is even
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# Calculate area of rectangle
def area(length, width):
    return length * width

room_area = area(10, 12)
print(f"Room area: {room_area} sq ft")

# Temperature converter
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

temp_f = celsius_to_fahrenheit(25)
print(f"25°C is {temp_f}°F")

# Validate password
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

# ===================================
# VARIABLE SCOPE
# ===================================

# Variables inside functions are LOCAL
def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # Error! x doesn't exist outside the function

# Global variables
name = "Connor"  # Global variable

def print_name():
    print(name)  # Can read global variables

print_name()

# ===================================
# DOCSTRINGS (Function Documentation)
# ===================================

def add(a, b):
    """
    Add two numbers together.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b

# You can view the docstring
print(add.__doc__)
