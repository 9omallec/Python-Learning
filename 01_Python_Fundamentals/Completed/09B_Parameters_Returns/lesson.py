"""
===========================================
LESSON 09B: FUNCTION PARAMETERS & RETURNS
===========================================

Building on basic functions, learn how to:
- Pass data INTO functions (parameters)
- Get data OUT of functions (return values)
- Use multiple parameters
- Return multiple values
"""

# ============================================
# PART 1: PARAMETERS (INPUT)
# ============================================
# Parameters let you pass data into a function

def greet(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!


# Multiple parameters
def add(a, b):
    """Function with two parameters"""
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)   # Output: 5 + 3 = 8
add(10, 7)  # Output: 10 + 7 = 17


# ============================================
# PART 2: RETURN VALUES (OUTPUT)
# ============================================
# Return sends data back from the function

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20

# You can use returned values directly
print(multiply(3, 7))  # Output: 21

# Return vs Print
def print_sum(a, b):
    print(a + b)  # Just prints, returns None

def return_sum(a, b):
    return a + b  # Returns the value

x = print_sum(2, 3)   # Prints: 5
print(x)              # Prints: None (function didn't return anything)

y = return_sum(2, 3)  # Doesn't print anything
print(y)              # Prints: 5 (the returned value)


# ============================================
# PART 3: RETURN MULTIPLE VALUES
# ============================================
# Functions can return multiple values as a tuple

def get_min_max(numbers):
    """Returns both minimum and maximum"""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 9


def divide_with_remainder(a, b):
    """Returns quotient and remainder"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")  # Output: 17 ÷ 5 = 3 remainder 2


# ============================================
# EXERCISES
# ============================================

# Exercise 1: Rectangle Area
# Write a function that takes length and width, returns the area
def calculate_area(length, width):
    return length * width

calculate_area(5, 10)


# Test it:
# area = calculate_area(5, 3)
# print(area)  # Should print: 15


# Exercise 2: Temperature Converter
# Write a function that converts Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32
def celsius_to_fahrenheit(celsius):
    temp_f = (celsius * 9 / 5) + 32
    return temp_f

celsius_to_fahrenheit(15)

# Test it:
temp_f = celsius_to_fahrenheit(0)
print(temp_f)  # Should print: 32.0
temp_f = celsius_to_fahrenheit(100)
print(temp_f)  # Should print: 212.0


# Exercise 3: Circle Calculations
# Write a function that takes radius and returns both area and circumference
# Area = π * r²
# Circumference = 2 * π * r
# Use 3.14159 for π
def circle_stats(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

# Test it:
area, circumference = circle_stats(5)
print(f"Area: {area}, Circumference: {circumference}")


# Exercise 4: Grade Calculator
# Write a function that takes a score (0-100) and returns a letter grade:
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80 and score < 90:
        return "B"
    if score >= 70 and score < 80:
        return "C"
    if score >= 60 and score < 70:
        return "D"
    else:
        return "F"

# Test it:
print(get_grade(95))  # Should print: A
print(get_grade(82))  # Should print: B
print(get_grade(58))  # Should print: F


# Exercise 5: String Info
# Write a function that takes a string and returns:
# - length, number of vowels, number of consonants
def string_info(text):
    length = len(text)
    vowel_count = 0
    consonants_count = 0
    for char in text:
        if char.lower() in 'aeiou':
            vowel_count += 1
        elif char.isalpha():
            consonants_count += 1
    return length, vowel_count, consonants_count
# Test it:
length, vowel_count, consonants_count = string_info("Hello World")
print(f"Length: {length}, Vowels: {vowel_count}, Consonants: {consonants_count}")


# Exercise 6: List Statistics
# Write a function that takes a list of numbers and returns:
# - sum, average, count
def list_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return total, avg, count

# Test it:
total, avg, count = list_stats([10, 20, 30, 40, 50])
print(f"Sum: {total}, Average: {avg}, Count: {count}")


# Exercise 7: Password Validator
# Write a function that checks if a password is strong
# Returns True if: length >= 8, has uppercase, has lowercase, has digit
# Returns False otherwise
def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit

# Test it:
print(is_strong_password("Hello123"))  # Should print: True
print(is_strong_password("weak"))      # Should print: False


# Exercise 8: Prime Checker
# Write a function that returns True if a number is prime, False otherwise
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) +1, 2):
        if n % i == 0:
            return False
    return True


# Test it:
print(is_prime(7))   # Should print: True
print(is_prime(10))  # Should print: False


# Exercise 9: Fibonacci
# Write a function that returns the nth Fibonacci number
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(2, n + 1):
        next_num = previous + current
        previous = current
        current = next_num

    return current

# Test it:
print(fibonacci(0))  # Should print: 0
print(fibonacci(5))  # Should print: 5
print(fibonacci(10)) # Should print: 55


# Exercise 10: Shopping Cart Total
# Write a function that takes a list of prices and a tax rate (0.0-1.0)
# Returns subtotal, tax amount, and total
def calculate_total_solution(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

# Test it:
subtotal, tax, total = calculate_total_solution([10.00, 20.00, 15.50], 0.08)
print(f"Subtotal: ${subtotal}, Tax: ${tax:.2f}, Total: ${total:.2f}")


"""
===========================================
SOLUTIONS
===========================================
"""

# Solution 1
def calculate_area_solution(length, width):
    return length * width


# Solution 2
def celsius_to_fahrenheit_solution(celsius):
    return (celsius * 9/5) + 32


# Solution 3
def circle_stats_solution(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference


# Solution 4
def get_grade_solution(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# Solution 5
def string_info_solution(text):
    length = len(text)
    vowels = sum(1 for char in text.lower() if char in 'aeiou')
    consonants = sum(1 for char in text.lower() if char.isalpha() and char not in 'aeiou')
    return length, vowels, consonants


# Solution 6
def list_stats_solution(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count if count > 0 else 0
    return total, avg, count


# Solution 7
def is_strong_password_solution(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit


# Solution 8
def is_prime_solution(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Solution 9
def fibonacci_solution(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


# Solution 10
def calculate_total_solution(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total
