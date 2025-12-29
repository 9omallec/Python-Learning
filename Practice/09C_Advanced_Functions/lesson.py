"""
===========================================
LESSON 09C: ADVANCED FUNCTIONS
===========================================

Learn advanced function concepts:
- Default parameters
- Variable-length arguments (*args, **kwargs)
- Scope (local vs global)
- Lambda functions
- Functions as arguments
"""

# ============================================
# PART 1: DEFAULT PARAMETERS
# ============================================
# Parameters can have default values

def greet(name, greeting="Hello"):
    """greeting has a default value"""
    print(f"{greeting}, {name}!")

greet("Alice")                # Output: Hello, Alice!
greet("Bob", "Hi")           # Output: Hi, Bob!
greet("Charlie", "Howdy")    # Output: Howdy, Charlie!


def power(base, exponent=2):
    """Square by default, or any power"""
    return base ** exponent

print(power(5))      # Output: 25 (5²)
print(power(5, 3))   # Output: 125 (5³)
print(power(2, 10))  # Output: 1024 (2¹⁰)


# ============================================
# PART 2: VARIABLE-LENGTH ARGUMENTS (*args)
# ============================================
# *args lets you pass any number of arguments

def sum_all(*numbers):
    """Sum any number of values"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # Output: 6
print(sum_all(10, 20, 30, 40))    # Output: 100
print(sum_all(5))                 # Output: 5


def print_items(*items):
    """Print all items passed"""
    for item in items:
        print(f"- {item}")

print_items("apple", "banana", "cherry")
# Output:
# - apple
# - banana
# - cherry


# ============================================
# PART 3: KEYWORD ARGUMENTS (**kwargs)
# ============================================
# **kwargs lets you pass any number of keyword arguments

def print_info(**info):
    """Print all key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC


def build_profile(name, **details):
    """Build a user profile"""
    profile = {'name': name}
    for key, value in details.items():
        profile[key] = value
    return profile

user = build_profile("Bob", age=30, job="Developer", city="SF")
print(user)
# Output: {'name': 'Bob', 'age': 30, 'job': 'Developer', 'city': 'SF'}


# Combining *args and **kwargs
def full_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

full_function("must have", 1, 2, 3, key1="value1", key2="value2")
# Output:
# Required: must have
# Args: (1, 2, 3)
# Kwargs: {'key1': 'value1', 'key2': 'value2'}


# ============================================
# PART 4: SCOPE (LOCAL VS GLOBAL)
# ============================================
# Variables inside functions are local

counter = 0  # Global variable

def increment():
    counter = 1  # This creates a NEW local variable
    print(f"Inside function: {counter}")

increment()           # Output: Inside function: 1
print(f"Global: {counter}")  # Output: Global: 0 (unchanged!)


# Using global keyword
score = 0

def add_points():
    global score  # Now we can modify the global variable
    score += 10

add_points()
print(score)  # Output: 10

add_points()
print(score)  # Output: 20


# ============================================
# PART 5: LAMBDA FUNCTIONS
# ============================================
# Small anonymous functions written in one line

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))          # Output: 25
print(square_lambda(5))   # Output: 25


# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# Lambda with if-else
max_value = lambda a, b: a if a > b else b
print(max_value(10, 5))  # Output: 10


# ============================================
# PART 6: FUNCTIONS AS ARGUMENTS
# ============================================
# Functions can be passed to other functions

def apply_operation(x, y, operation):
    """Apply the operation function to x and y"""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))       # Output: 8
print(apply_operation(5, 3, multiply))  # Output: 15


# Using lambda as argument
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Sort by custom key
words = ["apple", "pie", "zoo", "at"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  # Output: ['at', 'pie', 'zoo', 'apple']


# ============================================
# EXERCISES
# ============================================

# Exercise 1: Default Parameters - Greeting Card
# Write a function that creates a greeting card message
# Parameters: recipient (required), occasion (default: "Birthday"), sender (default: "Anonymous")
def create_card(recipient, occasion="Birthday", sender="Anonymous"):
    pass  # Your code here

# Test it:
# print(create_card("Mom"))
# print(create_card("Dad", "Anniversary", "Your Kids"))


# Exercise 2: *args - Find Maximum
# Write a function that finds the maximum of any number of values
def find_max(*numbers):
    pass  # Your code here

# Test it:
# print(find_max(1, 5, 3, 9, 2))  # Should print: 9
# print(find_max(10, 20))         # Should print: 20


# Exercise 3: *args - Average Calculator
# Write a function that calculates average of any number of grades
def calculate_average(*grades):
    pass  # Your code here

# Test it:
# print(calculate_average(90, 85, 92))        # Should print: 89.0
# print(calculate_average(100, 95, 88, 92))   # Should print: 93.75


# Exercise 4: **kwargs - Build HTML Tag
# Write a function that creates an HTML tag with attributes
# build_tag(tag_name, content, **attributes)
# Example: build_tag("a", "Click here", href="https://example.com", class_="link")
# Returns: '<a href="https://example.com" class="link">Click here</a>'
def build_tag(tag_name, content, **attributes):
    pass  # Your code here

# Test it:
# print(build_tag("a", "Click", href="https://google.com"))
# print(build_tag("div", "Hello", id="main", class_="container"))


# Exercise 5: Combining *args and **kwargs
# Write a function that creates a shopping receipt
# receipt(store_name, *items, tax_rate=0.08, discount=0)
def receipt(store_name, *items, tax_rate=0.08, discount=0):
    pass  # Your code here

# Test it:
# receipt("Bob's Store", 10.00, 20.00, 15.50, tax_rate=0.10)


# Exercise 6: Lambda - Temperature Converter
# Create a lambda function that converts Celsius to Fahrenheit
celsius_to_f = None  # Your lambda here

# Test it:
# print(celsius_to_f(0))    # Should print: 32.0
# print(celsius_to_f(100))  # Should print: 212.0


# Exercise 7: Lambda with Sorting
# Given a list of tuples (name, age), sort by age using lambda
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# sorted_people = sorted(people, key=???)  # Use lambda here

# Test it:
# print(sorted_people)  # Should print: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]


# Exercise 8: Function as Argument - Calculator
# Write a function that performs different operations on a list
# apply_to_list(numbers, operation) where operation is a function
def apply_to_list(numbers, operation):
    pass  # Your code here

# Test it:
# nums = [1, 2, 3, 4, 5]
# squared = apply_to_list(nums, lambda x: x ** 2)
# print(squared)  # Should print: [1, 4, 9, 16, 25]


# Exercise 9: Global Counter
# Create a function that counts how many times it's been called
# Use a global variable
call_count = 0

def track_calls():
    pass  # Your code here

# Test it:
# track_calls()  # Should print: Called 1 time(s)
# track_calls()  # Should print: Called 2 time(s)
# track_calls()  # Should print: Called 3 time(s)


# Exercise 10: Flexible Search
# Write a function that searches a list with flexible criteria
# search(items, *search_terms, case_sensitive=False)
# Returns items that contain ANY of the search terms
def search(items, *search_terms, case_sensitive=False):
    pass  # Your code here

# Test it:
# fruits = ["Apple", "Banana", "Cherry", "Avocado", "Blueberry"]
# print(search(fruits, "app", "berry"))  # Should find Apple, Blueberry


"""
===========================================
SOLUTIONS
===========================================
"""

# Solution 1
def create_card_solution(recipient, occasion="Birthday", sender="Anonymous"):
    return f"Happy {occasion}, {recipient}!\nFrom: {sender}"


# Solution 2
def find_max_solution(*numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


# Solution 3
def calculate_average_solution(*grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


# Solution 4
def build_tag_solution(tag_name, content, **attributes):
    attrs = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    if attrs:
        return f'<{tag_name} {attrs}>{content}</{tag_name}>'
    return f'<{tag_name}>{content}</{tag_name}>'


# Solution 5
def receipt_solution(store_name, *items, tax_rate=0.08, discount=0):
    print(f"===== {store_name} =====")
    subtotal = sum(items)
    print(f"Subtotal: ${subtotal:.2f}")
    discount_amount = subtotal * discount
    if discount > 0:
        print(f"Discount: -${discount_amount:.2f}")
    taxable = subtotal - discount_amount
    tax = taxable * tax_rate
    print(f"Tax: ${tax:.2f}")
    total = taxable + tax
    print(f"Total: ${total:.2f}")
    return total


# Solution 6
celsius_to_f_solution = lambda c: (c * 9/5) + 32


# Solution 7
people_solution = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people_solution = sorted(people_solution, key=lambda x: x[1])


# Solution 8
def apply_to_list_solution(numbers, operation):
    return [operation(num) for num in numbers]


# Solution 9
call_count_solution = 0

def track_calls_solution():
    global call_count_solution
    call_count_solution += 1
    print(f"Called {call_count_solution} time(s)")


# Solution 10
def search_solution(items, *search_terms, case_sensitive=False):
    results = []
    for item in items:
        item_check = item if case_sensitive else item.lower()
        for term in search_terms:
            term_check = term if case_sensitive else term.lower()
            if term_check in item_check:
                results.append(item)
                break
    return results
