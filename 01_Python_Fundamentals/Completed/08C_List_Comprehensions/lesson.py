# ===================================
# LESSON 8C: List Comprehensions
# ===================================

# List comprehensions are a Pythonic way to create lists
# They're shorter and often faster than loops
# This is an OPTIONAL advanced lesson!

# ===================================
# BASIC LIST COMPREHENSION
# ===================================

# OLD WAY - Using a loop
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# NEW WAY - List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Syntax: [expression for item in iterable]

# ===================================
# MORE EXAMPLES
# ===================================

# Create list of doubles
numbers = [1, 2, 3, 4, 5]
doubles = [n * 2 for n in numbers]
print(doubles)  # [2, 4, 6, 8, 10]

# Convert to uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Extract lengths
words = ["cat", "elephant", "dog", "butterfly"]
lengths = [len(word) for word in words]
print(lengths)  # [3, 8, 3, 9]

# ===================================
# LIST COMPREHENSION WITH IF
# ===================================

# OLD WAY - Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)  # [2, 4, 6, 8, 10]

# NEW WAY - List comprehension with condition
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Syntax: [expression for item in iterable if condition]

# ===================================
# MORE CONDITIONAL EXAMPLES
# ===================================

# Get only long words
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['elephant', 'butterfly']

# Get only passing scores
scores = [45, 78, 92, 55, 88, 61, 95]
passing = [score for score in scores if score >= 70]
print(passing)  # [78, 92, 88, 95]

# Get numbers divisible by 3
numbers = range(1, 21)
div_by_3 = [n for n in numbers if n % 3 == 0]
print(div_by_3)  # [3, 6, 9, 12, 15, 18]

# ===================================
# IF-ELSE IN LIST COMPREHENSION
# ===================================

# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Pass/Fail labels
scores = [45, 78, 92, 55, 88]
results = ["Pass" if s >= 70 else "Fail" for s in scores]
print(results)  # ['Fail', 'Pass', 'Pass', 'Fail', 'Pass']

# Cap values at 100
values = [85, 120, 95, 110, 75]
capped = [v if v <= 100 else 100 for v in values]
print(capped)  # [85, 100, 95, 100, 75]

# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]

# ===================================
# NESTED LIST COMPREHENSIONS
# ===================================

# Flatten a matrix (2D list to 1D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# ...

# ===================================
# PRACTICAL USES
# ===================================

# Extract file extensions
files = ["doc.txt", "image.png", "data.csv", "script.py"]
extensions = [f.split(".")[-1] for f in files]
print(extensions)  # ['txt', 'png', 'csv', 'py']

# Clean data - remove whitespace
messy = ["  hello", "world  ", "  python  "]
clean = [s.strip() for s in messy]
print(clean)  # ['hello', 'world', 'python']

# Parse numbers from strings
str_nums = ["10", "20", "30", "40"]
numbers = [int(n) for n in str_nums]
print(numbers)  # [10, 20, 30, 40]

# Get first letter of each name
names = ["Alice", "Bob", "Charlie", "Diana"]
initials = [name[0] for name in names]
print(initials)  # ['A', 'B', 'C', 'D']

# ===================================
# WHEN TO USE LIST COMPREHENSIONS
# ===================================

# ✓ USE when: Simple transformation or filtering
# ✓ USE when: Code is still readable
# ✗ AVOID when: Logic is complex (use normal loops)
# ✗ AVOID when: Readability suffers

# GOOD - Simple and clear
squares = [x**2 for x in range(10)]

# BAD - Too complex, hard to read
result = [x**2 if x % 2 == 0 else x**3 if x % 3 == 0 else x for x in range(20) if x % 5 != 0]

# ===================================
# COMPARISON
# ===================================

print("\nLoop vs Comprehension:")

# Using loop (5 lines)
result1 = []
for i in range(10):
    if i % 2 == 0:
        result1.append(i ** 2)

# Using comprehension (1 line)
result2 = [i ** 2 for i in range(10) if i % 2 == 0]

print(result1)  # [0, 4, 16, 36, 64]
print(result2)  # [0, 4, 16, 36, 64]
print("Same result!", result1 == result2)
